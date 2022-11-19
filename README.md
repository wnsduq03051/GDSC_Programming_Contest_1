# GDSC_Programming_Contest_1
문제:
낙낙
20XX년 11월 6일, 제 37회 GDSC Programming Contest가 개최되었습니다!

1회와 달리, 37회에는 많은 사람들의 오프라인 참여를 유도하기 위해 성수낙낙 뿐만이 아닌, 다른 장소도 섭외하여 개최하려고 합니다. 하지만 아무 장소나 섭외하게 된다면 대회의 위상이 떨어질 수 있으므로, 반드시 다음과 같은 조건을 만족하는 장소만 대여하려고 합니다.

장소를 영어로 표기하였을 때, 해당 문자열에서 일부 글자들을 지워 “nak” 라는 문자열을 만들 수 있다면, 우리는 이 장소가 낙 한 장소라고 부릅니다.
마찬가지로, “naknak” 이라는 문자열을 만들 수 있다면, 우리는 이 장소가 낙낙 한 장소라고 부릅니다.
마지막으로, 위와 같은 방법으로 “naknaknak” 이라는 문자열을 만들 수 있다면, 우리는 이 장소가 낙낙낙 한 장소라고 부를 겁니다.
어떤 장소를 빌릴 때, 그 장소가 낙낙 하지만 낙낙낙 하지 않은 장소인 경우에만 대여하려고 합니다.
섭외 가능한 건물들의 목록인 buildings 가 매개변수로 주어질 때, 각각의 건물들을 대여할지의 여부를 return 하는 solution 함수를 완성해주세요.


지시사항
제약조건
buildings 의 길이는 1 이상 100 이하입니다.
한 건물의 이름의 길이는 10 이상 1,000 입니다.
buildings 배열에 들어있는 모든 문자열의 길이는 최대 100,000 이하입니다.
buildings 배열에 들어있는 문자열은 알파벳 소문자 및 공백으로 구성되어 있습니다.
각각의 건물에 대해, 대여를 한다면 O 를, 대여를 하지 않는다면 X 를 담아서 반환해주세요.
입출력 예
buildings	result
[“sungsoo_naknak”, “sungsoo_naknaknak”, “sungsoo_nak”]	[“O”, “X”, “X”]
[“i_am_not_a_kim_and_not_awk”, “nananananakkkk”]	[“O”, “X”]
입출력 예 설명
입출력 예 #1
sungsoo_naknak 은 naknak을 포함하고 있으므로, 낙낙 합니다.
sungsoo_naknaknak 은 naknak을 포함하고 있으므로, 낙낙 하지만 naknaknak 을 포함하고 있으므로, 낙낙낙 합니다.
sungsoo_nak은 낙낙하지 않습니다.
입출력 예 #2
i_am_not_a_kim_and_not_awk 은 naknak을 포함하고 있으므로, 낙낙 합니다.
nananananakkkk 은 낙낙하지 않습니다.
