import ast
import astunparse
import hashlib

class name_change(ast.NodeTransformer) :
    # def visit_Name (self, node) :
    #     if node.id in ['print', 'self'] :
    #         node.id = node.id
    #     else :
    #         node.id = hashlib.sha256(node.id.encode()).hexdigest()
    #         if ord(node.id[0]) in range (48,58) :
    #             node.id = '_' + node.id 
    #         self.generic_visit(node)
    #     return node
    #     # node.attr = hashlib.sha256(node.attr.encode()).hexdigest()
    #     # if ord(node.attr[0]) in range (48,58) :
    #     #     node.attr = '_' + node.attr 
    #     # self.generic_visit(node)
    #     # return node
    # def visit_Attribute (self, node) :
    #     node.attr = hashlib.sha256(node.attr.encode()).hexdigest()
    #     if ord(node.attr[0]) in range (48,58) :
    #         node.attr = '_' + node.attr 
    #     self.generic_visit(node)
    #     return node
    def generic_visit(self, node):
        for field, old_value in ast.iter_fields(node):
            if type(old_value) == str :
                if old_value not in ['self', 'print', 'range', 're', 'math', 'datetime', 'MINYEAR', 'copy', 
                'Exception','and','exec','not','assert','finally','or','break','for','pass','class','from','print',
                'continue','global','raise','def','if','return','del','import','try','elif','in','while','else','is',
                'with','except','lambda','yield','True','False','None','self','struct', '__init__', 'locals', '__dict__',
                '__del__','__add__','__repr__','__len__','__file__','__all__','sys','os','dict','str','int','float','round','len','getcwd',
                'append','deepcopy','globals','doctest','testmod','warnings','warn','pop','getenv','platform','win32','linux2','match']:
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
    # def visit_Call(self, node) :
    #     for field, old_value in ast.iter_fields(node):
    #         if field != 'func' :
    #             if isinstance(old_value, list):
    #                 new_values = []
    #                 for value in old_value:
    #                     if isinstance(value, ast.AST):
    #                         value = self.visit(value)
    #                         if value is None:
    #                             continue
    #                         elif not isinstance(value, ast.AST):
    #                             new_values.extend(value)
    #                             continue
    #                     new_values.append(value)
    #                 old_value[:] = new_values
    #             elif isinstance(old_value, ast.AST):
    #                 new_node = self.visit(old_value)
    #                 if new_node is None:
    #                     delattr(node, field)
    #                 else:
    #                     setattr(node, field, new_node)
    #     return node

DP = ast.parse(open('./designs/DesignParameters.py').read())
DP_1 = name_change()
DP_out = DP_1.visit(DP)
DP_w = open('./designs/DesignParameters1.py','w')
DP_w.write(astunparse.unparse(DP_out))

DRC = ast.parse(open('./designs/DRC.py').read())
DRC_1 = name_change()
DRC_out = DRC_1.visit(DRC)
DRC_w = open('./designs/DRC1.py','w')
DRC_w.write(astunparse.unparse(DRC_out))

Stick = ast.parse(open('./designs/StickDiagram.py').read())
Stick_1 = name_change()
Stick_out = Stick_1.visit(Stick)
Stick_w = open('./designs/StickDiagram1.py','w')
Stick_w.write(astunparse.unparse(Stick_out))

GDS_EL = ast.parse(open('./gds_editor_ver3/gds_elements.py').read())
GDS_EL_1 = name_change()
GDS_EL_out = GDS_EL_1.visit(GDS_EL)
GDS_EL_w = open('./gds_editor_ver3/gds_elements1.py','w')
GDS_EL_w.write(astunparse.unparse(GDS_EL_out))

GDS_R = ast.parse(open('./gds_editor_ver3/gds_record.py').read())
GDS_R_1 = name_change()
GDS_R_out = GDS_R_1.visit(GDS_R)
GDS_R_w = open('./gds_editor_ver3/gds_record1.py','w')
GDS_R_w.write(astunparse.unparse(GDS_R_out))

GDS_STREAM = ast.parse(open('./gds_editor_ver3/gds_stream.py').read())
GDS_STREAM_1 = name_change()
GDS_STREAM_out = GDS_STREAM_1.visit(GDS_STREAM)
GDS_STREAM_w = open('./gds_editor_ver3/gds_stream1.py','w')
GDS_STREAM_w.write(astunparse.unparse(GDS_STREAM_out))

GDS_structure = ast.parse(open('./gds_editor_ver3/gds_structures.py').read())
GDS_structure_1 = name_change()
GDS_structure_out = GDS_structure_1.visit(GDS_structure)
GDS_structure_w = open('./gds_editor_ver3/gds_structures1.py','w')
GDS_structure_w.write(astunparse.unparse(GDS_structure_out))

gds_tags = ast.parse(open('./gds_editor_ver3/gds_tags.py').read())
gds_tags_1 = name_change()
gds_tags_out = gds_tags_1.visit(gds_tags)
gds_tags_w = open('./gds_editor_ver3/gds_tags1.py','w')
gds_tags_w.write(astunparse.unparse(gds_tags_out))

user_d = ast.parse(open('./gds_editor_ver3/user_define_exceptions.py').read())
user_d_1 = name_change()
user_d_out = user_d_1.visit(user_d)
user_d_w = open('./gds_editor_ver3/user_define_exceptions1.py','w')
user_d_w.write(astunparse.unparse(user_d_out))