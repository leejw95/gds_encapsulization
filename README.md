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

(Local terminal에서 실행)
```shell
docker container run -it (--rm -v 파일경로:컨테이너내부경로) intel/oneapi-hpckit
```
또는
```shell
docker restart <container name>
docker attach <container name>
```

## Usage for encoding and compile
0. 이 과정들은 Docker에서 함을 추천한다. (Windows 에서 실행시 Encode 에러가 발생하는 경우가 있음.)
1. 우선 Encode.py에 있는 method_list() 함수를 실행시켜, /generatorLib/ 디렉토리 내의 Class, method 들의 평문 list를 .pickle 파일로 추출한다.
    (위 Gen_list.pickle 파일은 추후 배포 디렉토리에 첨부하여야 한다.)
2. 추출 후, main_1() 함수를 실행시켜 /generatorLib/ 디렉토리 내의 파일들을 encrypt 시킨다.
3. 이후, ./auto_encrypted_test 에 미리 만들어둔 Makefile을 활용하여 cythonize, compile과정을 수행한다.

(Docker Shell에서 실행)
```shell
python Encode.py
cp ./Gen_list.pickle ./auto_encrypted_test
cd ./auto_encrypted_test
make cyt
make comp
```

신규로 추가해야할 파일 (new.py)들이 있으면, Encode.py에 원하는 python file만 지정해주고, 다음을 실행하여 준다.
추가적으로 개정된 pickle file을 생성해야하므로, Encode.py에 있는 method_list() 함수를 처음에 1회 실행해주어야 한다.

(Docker Shell에서 실행)
```shell
python Encode.py
cp ./Gen_list.pickle ./auto_encrypted_test
cd ./auto_encrypted_test
cython -3 new.py
make comp
```

## For Distribution
배포 시 준비해야 할 파일들
1. /auto_encrypted_test/build/lib.linux-x86_64-3.9 디렉토리 내에 .so (shared object) files
2. /auto_encrypted_test/Generator.py
3. Layermap file (cmos28lp_tech.layermap)
4. Gen_list.pickle file (Encode.py로 부터 생성된 파일)

Docker에서 local로 파일 복사 시 (Local terminal에서 실행)
```shell
docker cp <Container name>:<Container path> <Local Path>
```

## GDS Generation
1. 배포한 .so files, Generator.py, layermap file, pickle file을 새 docker에 이동시킨다.
이후 python Generator.py 실행.
2. 원하는 Generator 종류 입력.
3. Generator에서 실행시킬 함수 선택. 숫자로 입력하면 되며, 0번부터 시작이다.
4. 이후 Default 값들이 출력된 후, 순서대로 원하는 입력값을 대입하면 된다.
    이 때, None, True, False 값들은 소문자로 입력하여도 정상 인식한다.
    하지만 LVT, SLVT, 등 layer 값들은 모두 대문자 그대로 입력하여야 한다.
5. 'UserWarning...' 이 출력된다면 정상적으로 GDS file이 출력된 경우이며, 
    ERROR가 발생한 경우 정상적으로 출력되지 못한 경우이다.
6. 이후 Local에 GDS file을 복사하여 사용하면 된다.

Local에서 Docker로 파일 복사 시 (Local terminal에서 실행)
```shell
docker cp <Local Path> <Container name>:<Container path>
```

## Expiration Date
Encode.py, ./Encode_list/DesignParameters.py, ./Encode_list/StickDiagram.py, ./Encode_list/StickDiagram.py, ./Encode_list/gds_stream.py 
위 5개 file에 유효기간을 조정해주면 된다.

## Toy Example
test_generator.py 파일을 실행하면 gds 파일이 만들어짐 (이는 Framework 배포용)

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

## Encode 혹은 Cython 과정 오류 시
위 과정은 모든 file을 AST module을 통해 구문분석 후 각 변수들을 sha512 알고리즘을 통해 변환해주는 과정이다.
평문으로 표출되길 원하는 부분이 암호화되었거나, 암호화되길 원하는 부분이 평문으로 나타나는 경우 Encode.py에서
main_1() 함수의 test 구문만을 주석 해제 후, astunparse를 통해 원하는 구문의 구조가 ast의 어느 트리에 해당하는지 확인 후 
Encode.py 상단에서 수정해주어야 한다.
