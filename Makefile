CC = cython
OBJECTS = ./designs/StickDiagram.py ./designs/DesignParameters.py ./designs/DRC.py
OBJECTS1   =   ./gds_editor_ver3/gds_elements.py   ./gds_editor_ver3/gds_stream.py  ./gds_editor_ver3/gds_structures.py   ./gds_editor_ver3/gds_tags.py ./gds_editor_ver3/gds_record.py
cyt :
         $(CC) $(OBJECTS) ; $(CC) $(OBJECTS1)
# clean :
#         rm *.so ; cd gds_editor_ver3 ; rm *.so
# clean2 :
#         rm   DRC.py   DesignParameters.py   StickDiagram.py   *.c   *.pyc   ;   cd gds_editor_ver3 ; rm *.py *.c *.pyc