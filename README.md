# gds_editor encapsulization
GDSII Editor Engine 배포를 위해 변수 암호화와 cython으로 c로 변환 후 컴파일 하는 과정을 수행함.

##prerequisite
* Docker 사용 또는 Intel HPC
* Docker 사용 또는 Intel python (3.7)
*

##Docker 사용시
intel/oneapi-hpckit 이미지를 이용하면 손쉽게 Intel HPC, Intel python 사용이 가능함.
```shell
docker container run -it --rm -v 파일경로:컨테이너내부경로 intel/oneapi-hpckit
```

##Usage for encoding and compile
```shell
python Encode.py
cd ./auto_encrypted_test
make cyt
make comp
```

##Toy Example
test_generator.py 파일을 실행하면 gds 파일이 만들어짐
