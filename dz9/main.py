from player import Player
from utils import load_random_word

print("Введите имя игрока")
player_name = input()
player = Player(player_name)

word = load_random_word()

print(f"Привет, {player.name}")
print(f"Составьте {len(word.subwords)} слов из слова {word.word.upper()}")
print("Слова должны быть не короче 3 букв")
print("Чтобы закончить игру, угадайте все слова или нажмите \"stop\"")
print("Поехали, ваше первое слово?")

while len(player.user_subwords) != len(word.subwords):
    input_word = input().lower()
    if len(input_word) < 3:
        print("слишком короткое слово")
        continue
    if input_word == "stop" or input_word == "стоп":
        break
    if not word.is_subwords(input_word):
        print("неверно")
        continue
    if player.is_word_in_user_subwords(input_word):
        print("уже использовано")
        continue

    player.add_word_in_subwords(input_word)
    print("верно")

print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")




