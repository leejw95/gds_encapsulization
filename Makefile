CC = cython
OBJECTS = StickDiagram.py DesignParameters.py DRC.py
OBJECTS1 = gds_elements.py gds_stream.py gds_structures.py gds_tags.py gds_record.py
cyt :
    cd designs; $(CC) $(OBJECTS) ; cd ../gds_editor_ver3; $(CC) $(OBJECTS1)
clean :
    rm *.so ; cd gds_editor_ver3 ; rm *.so
clean2 :
    rm   DRC.py   DesignParameters.py   StickDiagram.py   *.c   *.pyc   ;   cd gds_editor_ver3 ; rm *.py *.c *.pyc