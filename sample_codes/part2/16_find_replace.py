sentence="Hello, how are you?"
position=sentence.find("how")
print(f"字串 'how' 的位置：{position}")
not_found_position=sentence.find("good")
print(f"字串 'good' 的位置：{not_found_position}")

sentence1="I like apples, but I don't like oranges."
new_sentence=sentence1.replace("apples","bananas")
print(f"替換後的句子：{new_sentence}")
