# SwiLan
If you use multiple keyboard languages in your system, you must have forgotten to change the keyboard language and type text in another language. In this case, you have text that has no specific meaning.
For example, I type this text in my keyboard:
```
Hello World!
```
Oh no, I forgot to **change my keyboard language**.This is the typed text in persian:
```
آثممخ صخقمی!
```
At this time you can call SwiLan as an **easy way :)**
# Basic Usage
To use Swilan you sould first import it:
```Python
import * from Swilan
```

Then, call the `Swilan()` function to switch the language of your text:
```python
wrong_text = "آثممخ صخقمی!"
modified_text = Swilan(wrong_text)
print(modified_text)
```
Congratulations, this is the result:
```
Hello World!
```

# Professional use
This program detects the text language by characters by default. but if you know the language of your text, you can manually use the function for that language. for example:
```python
wrong_text = "sghl nkdh!"
modified_text = ToPersian(wrong_text)
# Also for Persian text: ToEnglish(wrong_text)

print(modified_text)
```
The result is:
```
سلام دنیا!
```
