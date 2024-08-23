from deep_translator import GoogleTranslator

# Use any translator you like, in this example GoogleTranslator
translated = GoogleTranslator(source='auto', target='es').translate("Hello!")  # output -> Weiter so, du bist großartig
print(translated)