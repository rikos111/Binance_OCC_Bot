import os
if(os.path.exists("binance_f/privateconfig.py")):
    from binance_f.privateconfig import *
    g_api_key = p_api_key
    g_secret_key = p_secret_key
else:
    g_api_key = "AIWpaNgtcDMM8LV8ZQkcnCEIsfgmHkVxJChftLlVbUroKvBLZfF6dOSHd8isGLXL"
    g_secret_key = "u9khIRbhOb61eEdmjXRjTGYy8T7eFFNN4jsVTmkknsIDMAyCkdOPj8UiqRUH88XP"


g_account_id = 12345678



