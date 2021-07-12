import ast, astunparse, hashlib

class cvisitor(ast.NodeTransformer):
    def generic_visit(self, node):
        for field, old_value in ast.iter_fields(node):
            if field in ['name', 'id', 'attr']:
                if old_value not in ['self', 'print', 'range']:
                    sha = hashlib.new('sha256')
                    sha.update(old_value.encode())
                    hash_str = sha.hexdigest()
                    if hash_str[0].isdigit():
                        hash_str = '_' + hash_str
                    node.__dict__[field] = hash_str
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, ast.AST):
                        value = self.visit(value)
                        if value is None:
                            continue
                        elif not isinstance(value, ast.AST):
                            new_values.extend(value)
                            continue
                    new_values.append(value)
                old_value[:] = new_values
            elif isinstance(old_value, ast.AST):
                new_node = self.visit(old_value)
                if new_node is None:
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
        return node

f = open('./block_layer.py').read()
parsed = ast.parse(f)
cv = cvisitor()
out = cv.visit(parsed)
print(astunparse.unparse(out))
