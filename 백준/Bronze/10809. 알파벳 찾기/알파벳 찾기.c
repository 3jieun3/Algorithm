#include <stdio.h>
#include <string.h>

int main() {
	int alph[26]; // 알파벳은 26개 0-a(아스키 97), 25-z(아스키 122)
	memset(alph, -1, sizeof(int) * 26); // -1로 배열 초기화

	char word[101];
	scanf("%s", word);

	for (int i = 0; i < strnlen(word,100); i++) {
		int asc = word[i]; // 알파벳의 아스키코드
		int index = asc - 97; // 아스키 코드 - 97 이 alph 의 인덱스
		
		if (alph[index] == -1) alph[index] = i;
	}
	for (int j = 0; j < 26; j++) printf("%d ", alph[j]);
}