from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
import random

def read_names_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.read().splitlines()
    return names

# Lokasi untuk menyimpan sesi
session_path = "D:/selenimu2"
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={session_path}")
# chrome_options.add_argument("--headless")
# Inisialisasi WebDriver dengan opsi sesi
# Inisialisasi instance WebDriverWait



# Membuat folder jika belum ada
os.makedirs(session_path, exist_ok=True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)  # Misalnya, waktu maksimum tunggu adalah 10 detik

while True:
    # Set opsi untuk menyimpan sesi
    # Buka situs web
    url = "https://carv.io/profile/Vannn"
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)

    # Klik elemen pertama
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/header/div/div/div[3]/div[2]/div[2]/div[2]/div/span'))).click()
    except TimeoutException:
        print("Timed out waiting for element to be clickable")

    # Klik elemen kedua setelah mengklik elemen pertama
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div[4]/button'))).click()
    except TimeoutException:
        print("Timed out waiting for second element to be clickable")

    # Tunggu hingga tab baru dengan nama "X" terbuka
    try:
        new_tab_window_handle = wait.until(EC.new_window_is_opened(driver.window_handles))
        new_tab_name = driver.window_handles[-1]
        # Beralih ke tab baru
        driver.switch_to.window(new_tab_name)
        # Klik elemen pada tab baru
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div'))).click()
        # Tambahkan waktu tidur setelah setiap klik
        time.sleep(1)
    except TimeoutException:
        print("Timed out waiting for element in new tab to be clickable")

    # Klik elemen-elemen berikutnya
# Klik elemen-elemen berikutnya
    elements_to_click = [
    '/html/body/div[2]/div[3]/div/div/div[3]/button[1]',
    '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/button',
    '//*[@id="app"]/div[1]/header/div/div/div[3]/div[2]/div[2]/div[3]/div/div',
    '/html/body/div[2]/div[3]/ul/li[3]',
    '/html/body/div[1]/div[1]/div[1]/div/div/div[1]/div[1]/div'
]

# Iterasi melalui elemen dan coba klik
    for element_xpath in elements_to_click:
        while True:

            try:

                # Tunggu hingga elemen yang menutupi hilang

                wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="Toastify__toast-container"]')))

                # Coba klik elemen
                wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()
                break  # Keluar dari loop jika berhasil diklik
            except Exception as e:
                print(f"Failed to click element {element_xpath}: {str(e)}")

    # Pindah ke iframe dan hapus konten di dalam textarea
    iframe_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/form/div[2]/div[2]/div[1]/div/div/iframe'
    textarea_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/form/div[2]/div[2]/div[1]/div/div/input'

    # Hapus konten di dalam textarea
    while True:
        try:
            textarea = wait.until(EC.element_to_be_clickable((By.XPATH, textarea_xpath)))
            for _ in range(30):
                textarea.send_keys(Keys.BACKSPACE)
            break  # Keluar dari loop jika berhasil dihapus
        except Exception as e:
            print(f"Failed to clear textarea: {str(e)}")

    # Pindah ke iframe dan hapus konten di dalam textarea
    textarea_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/form/div[2]/div[2]/div[1]/div/div/input'

    # Hapus konten di dalam textarea
    try:
        textarea = wait.until(EC.element_to_be_clickable((By.XPATH, textarea_xpath)))
        for _ in range(30):
            textarea.send_keys(Keys.BACKSPACE)
        # Ambil nama random dari file teks lokal dan tuliskan di textarea
        first_names = read_names_from_file("C:\\Users\\Administrator\\Documents\\GitHub\\HotWalletBot\\first-names.txt")
        midle_names = read_names_from_file("C:\\Users\\Administrator\\Documents\\GitHub\\HotWalletBot\\middle-names.txt")
        random_name = f"{random.choice(first_names)}{random.choice(midle_names)}"
        textarea.send_keys(random_name)
    except TimeoutException:
        print("Timed out waiting for textarea to be present or clickable")

    # Keluar dari iframe
    driver.switch_to.default_content()

    # Klik tombol save
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/form/div[1]/button'))).click()
        # Tambahkan waktu tidur setelah setiap klik
        time.sleep(3)
    except TimeoutException:
        print("Timed out waiting for save button to be clickable")

    # Klik elemen setelah tombol save
    elements_after_save = [
        '//*[@id="app"]/div[1]/header/div/div/div[3]/div[2]/div[2]/div[3]/div/div',
        '/html/body/div[2]/div[3]/ul/li[6]'
    ]

    # Iterasi melalui elemen dan coba klik
    for element_xpath in elements_after_save:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()
            # Tambahkan waktu tidur setelah setiap klik
            
        except Exception as e:
            print(f"Failed to click element {element_xpath}: {str(e)}")
    time.sleep(3)
    print("Success Follow")
    driver.close()


           

# Tutup browser
