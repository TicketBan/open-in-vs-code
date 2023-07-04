import winreg
import ctypes

def remove_context_menu_entry():
    try:
        # Открываем ключ реестра для контекстного меню директорий
        key_path = r"Directory\Background\shell\OpenVsCode"
        reg_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_ALL_ACCESS)

        # Удаляем ключ реестра
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key_path)

        # Выводим сообщение об успешном удалении
        ctypes.windll.user32.MessageBoxW(0, "Опция успешно удалена из контекстного меню.", "Успех", 0)
    except Exception as e:
        # Выводим сообщение об ошибке при удалении
        ctypes.windll.user32.MessageBoxW(0, f"Произошла ошибка при удалении опции из контекстного меню: {str(e)}", "Ошибка", 0)

# Вызываем функцию для удаления опции из контекстного меню
remove_context_menu_entry()
