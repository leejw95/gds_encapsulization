# gds_editor encapsulization
GDSII Editor Engine 배포를 위해 변수 암호화와 cython으로 c로 변환 후 컴파일 하는 과정을 수행함.

## prerequisite
* Docker 사용 또는 Intel HPC
* Docker 사용 또는 Intel python (3.8)
* Docker Image  "intel/oneapi-hpckit" (Recommended)
* Docker 설치 및 사용법은 http://pyrasis.com/Docker/Docker-HOWTO 참조


## Docker 사용시
intel/oneapi-hpckit 이미지를 이용하면 손쉽게 Intel HPC, Intel python 사용이 가능함.
Windows 환경에선 Docker_Desktop 설치.
```shell
docker container run -it (--rm -v 파일경로:컨테이너내부경로) intel/oneapi-hpckit
```

## Usage for encoding and compile
0. 이 과정들은 Docker에서 함을 추천한다. (Windows 에서 실행시 Encode 에러가 발생하는 경우가 있음.)
1. 우선 Encode.py에 있는 method_list() 함수를 실행시켜, /generatorLib/ 디렉토리 내의 Class, method 들의 평문 list를 .pickle 파일로 추출한다.
2. 추출 후, main_1() 함수를 실행시켜 /generatorLib/ 디렉토리 내의 파일들을 encrypt 시킨다.
3. 이후, ./auto_encrypted_test 에 미리 만들어둔 Makefile을 활용하여 cythonize, compile과정을 수행한다.

```shell
python Encode.py
cd ./auto_encrypted_test
make cyt
make comp
```

## Toy Example
test_generator.py 파일을 실행하면 gds 파일이 만들어짐

## For Distribution
배포 시 준비해야 할 파일들
1. /auto_encrypted_test/build/lib.linux-x86_64-3.9 디렉토리 내에 .so (shared object) files
2. /auto_encrypted_test/Generator.py
3. Layermap file (cmos28lp_tech.layermap)
4. Gen_list.pickle file (Encode.py로 부터 생성된 파일)

## Expiration Date
Encode.py를 통해 조절이 가능하다.

## SHA256 Hashing
본 Encrypt에 사용된 알고리즘은 SHA256으로, 기본적으로 decode는 불가능한 구조이다.
따라서 오류가 발생했거나, 디버깅할 때 사용하는 용도로 ./Trans.py를 만들어두었다.
python console 실행 후, 
```Python
import Trans
a = Trans.Transfer()
a.change('string')
```
을 통하여 원하는 string의 hash 값을 알 수 있다.



Last updated 220711 Junung Choi