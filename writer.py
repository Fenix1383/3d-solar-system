import pygame

text = ''
def input_text(event):
                global text
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Обрабатываем ввод при нажатии Enter
                        result = text
                        text = ''
                        return result
                    
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        # Добавляем только цифры и точку
                        if event.unicode.isdigit() or event.unicode == '.':
                            text += event.unicode
                    print(text)
                    return None
