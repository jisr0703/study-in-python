### 백준 6566번
### 애너그램 그룹
#### 문제
평생 영어 단어를 암기한 준민이는 단어를 애너그램 그룹으로 나누려고 한다.

단어 w가 단어 v의 애너그램이 되려면, 단어 w의 알파벳 순서를 바꿔서 v를 만들 수 있어야 한다.\
이렇게 애너그램인 단어들을 묶어서 애너그램 그룹이라고 한다.\
그룹의 크기는 그 그룹에 포함된 단어의 수이다.

단어가 주어졌을 때, 크기가 가장 큰 애너그램 그룹 다섯 개를 구하는 프로그램을 작성하시오.

---
#### 입력
입력은 최대 30,000 줄로 이루어져 있고, 각 줄에는 알파벳 소문자로 이루어진 단어가 하나씩 주어진다.\
입력은 EOF로 끝난다. 

---
#### 출력
크기가 가장 큰 애너그램 다섯 개를 출력한다.\
만약, 그룹의 수가 다섯개보다 작다면, 모두 출력한다.\
그룹은 크기가 감소하는 순으로, 크기가 같을 때는 각 그룹에서 가장 사전 순으로 앞서는 단어의 사전 순으로 출력한다.

각 그룹을 출력할 때, 크기와 포함된 단어를 출력하며, 단어는 사전 순으로 출력해야 한다.\
같은 단어는 한 번만 출력한다.

---
#### 예제 입력 1 
undisplayed\
trace\
tea\
singleton\
eta\
eat\
displayed\
crate\
cater\
carte\
caret\
beta\
beat\
bate\
ate\
abet
#### 예제 출력 1 
Group of size 5: caret carte cater crate trace .\
Group of size 4: abet bate beat beta .\
Group of size 4: ate eat eta tea .\
Group of size 1: displayed .\
Group of size 1: singleton .

#### ex
apply\
paply\
apple\
armytau\
aamyurt\
amayurt\
amayrut\
ayamrut\
ataryum\
aratyum\
aartyum\
atrayum\
atraymu\
aartyum\
aartymu\
amayrut\
amyarut\
maayrut\
mayarut\
tarayum\
taraymu\
taryaum\
taryamu\
ratayum\
rataymu\
ratyaum\
ratyamu\
artayum\
artaymu\
artyaum\
argents\
strange\
garnets\
nagrest\
nagerst\
rangset\
tangsre\
gnatsre\
angstre\
tangres\
gnatres\
gartens\
garsent\
garnets\
garnest\
ragtens\
ragsent\
ragnets\
ragnest\
garsnet\
garsten\
ragsnet\
ragsten\
sagtern\
sagrent\
gastern\
gasrent\
addgirt\
addtrig\
addgrit\
dadgirt\
dadtrig\
dadgrit\
gaddirt\
dartdig\
dratdig\
tadgrid\
tadgird\
rangets\
antserg\
tanserg\
tanergs\
antergs\
artyamu\
rayatum\
rayatmu\
atayrum\
atyarum\
tauaymr\
tauyamr\
matuary\
lapep\
papel

---
#### 출처
https://www.acmicpc.net/problem/6566