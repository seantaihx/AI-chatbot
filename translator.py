from deep_translator import GoogleTranslator

def translate(text: str, source: str, target: str) -> str:
    return GoogleTranslator(source=source, target=target).translate(text)