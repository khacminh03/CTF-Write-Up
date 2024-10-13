from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
import base64
def decodeb64(encoded_string):
    reversed_string = encoded_string[::-1]
    
    replaced_string = reversed_string.replace('-', 'C').replace('_', 'E')
    
    padding_needed = len(replaced_string) % 4
    if padding_needed:
        replaced_string += '=' * (4 - padding_needed)
    return replaced_string
def decrypt(encrypted_data, key1):
    try:
        sha256 = SHA256.new()
        sha256.update(key1.encode('utf-8'))
        key = sha256.digest()
        
        encrypted_data = base64.b64decode(encrypted_data)
        
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        print("IV:", iv.hex())
        print("Ciphertext:", ciphertext.hex())
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        decrypted_data = cipher.decrypt(ciphertext)

        print("Decrypted data before unpadding:", decrypted_data.hex())
        
        decrypted_data = unpad(decrypted_data, AES.block_size)
        print("found: " + decrypted_data.decode('utf-8'))
        return decrypted_data.decode('utf-8')
    
    except (ValueError, KeyError) as e:
        print(f"Decryption failed: {e}")
        return None
flag = {}
data = {
    "Mmbl5-d4RnLx81ZhxmZ" : "0NaXoN6fZexANHcU0Q PtJtipYzI1MWcVGsKGQGi4v/",
    "j5WZuQHe05-Mx81ZhxmZ" : "AP6WHYj/iIeVJpLYXKZDjVLsWxyKbp1UGbApg8FeIzy",
    "j5WZuQHe05SMx81ZhxmZ" : "sdbNtnSpme/IKsR8lnccrkrUQ8LnmG9Hre ZPu9pzfI",
    "j5WZuQHe05SMx81ZhxmZ" : "sdbNtnSpme/IKsR8lnccrkrUQ8LnmG9Hre ZPu9pzfI",
    "j5WZuQHe05iMx81ZhxmZ" : "IPQButt ZPszbfnFuxcwm8k7xsIW9UGyHa9ni/IHu0O",
    "j5WZuQHe05yMx81ZhxmZ" : "UAOq1KVjPH2Wgewl8tyRwIhXLM-adWVTh0AjnTGUk-i",
    "j5WZuQHe05-Nx81ZhxmZ" : "oX9rxi jGLsyYqFZ6HXnZZw/QJod5Z _QT9kPr_SjSf",
    "j5WZuQHe05SNx81ZhxmZ" : "49gqimKu1B11q9h5bOOxybdxiSqwdN6YdOrPHGHf_e ",
    "j5WZuQHe05iNx81ZhxmZ" : "MSsr5rHr6DGetJzYdi -94kFFbBk briOAm7s2OXpdu",
    "j5WZuQHe05yNx81ZhxmZ" : "At eeUxAhPUl8K87Dihj1ca_z-aK7wtWm_kP0y4xewt",
    "j5WZuQHe05-Ox81ZhxmZ" : "ISOWbQnQ9zmXmjRSpd6b1YGSdIH7/FX4q2dZSvgaUtv",
    "j5WZuQHe05SOx81ZhxmZ" : "M7PI81by1P7N_O3cXaaVQZPf/-/ -TKNSYuuxWLrM  ",
    "Mmbl5-d4RnLy81ZhxmZ" : "Iz8pc9b88c1mOQHmc1hH5 xRDVFsPzL___qz1F-L724",
    "j5WZuQHe05-My81ZhxmZ" : "oxyTKzWBhT3k6_DXdk8w/vdQqoNADs33 1uofd1ag85",
    "j5WZuQHe05SMy81ZhxmZ" : "8ZM5IvDhvUe3oyorBcLNVGn8jHkeV1ugcw7YLkkrsOh",
    "j5WZuQHe05iMy81ZhxmZ" : "IUABjgWWScWKL61QX6SL1ZInpgTraKhUlsnRwftK51w",
    "j5WZuQHe05yMy81ZhxmZ" : "AjqTGzWp1NU_c3osnj5UiMqoSjyr cWS1zRkPraXZia",
    "j5WZuQHe05-Ny81ZhxmZ" : "cVjuho2jDb52OThxF-x-hU4g/_f3UfcbnOjW4rV8/8B",
    "j5WZuQHe05SNy81ZhxmZ" : "YY5ual0Zjw2LQRl3cMkqbXVRD/ccj8N1nKypZY chbh",
    "j5WZuQHe05iNy81ZhxmZ" : "_uDVjd009Xph0iNy5jFbZu-G r9_VTWtd8bn/WmhHa1",
    "j5WZuQHe05yNy81ZhxmZ" : "oq45d7S6pe_Ow7WPz95_/ceoLpl7eTyTl-B ukcaDzZ",
    "j5WZuQHe05-Oy81ZhxmZ" : "wfK8MdOj8TVV7URziByBOKeaAF6q-gSJisvJqur2bhc",
    "j5WZuQHe05SOy81ZhxmZ" : "sAciFmeJz9eN-Tp9VXb4TVar_9Gb/72uGa/RVrh_IQu",
    "Mmbl5-d4RnLz81ZhxmZ" : "IAjJSPH1fgXSn659HaDJu9Tdob60WIocHOc1Kfa-IkY",
    "j5WZuQHe05-Mz81ZhxmZ" : "8Gd2ZYvnhuZS9sPs3zZ_QRAIPIixf9un046KTDzfA L",
    "j5WZuQHe05SMz81ZhxmZ" : "sZVwZ1WkJOb4o9uhLjAx58cMZ5VNggXTrDaywWuNwx2",
    "j5WZuQHe05iMz81ZhxmZ" : "I4PPy59X8GiVHnU_a_saMvGWbqPMOiHpRwtY5kadUPF",
    "j5WZuQHe05yMz81ZhxmZ" : "8cnQt_79-/l4G5I3UQs0eRUyoGB6rdSXlJe-ZLqiaj ",
    "j5WZuQHe05-Nz81ZhxmZ" : "MNojovs4bjD _O0ReYV8B3tXWet/gGO9Vmv/h9TRI1M",
    "j5WZuQHe05SNz81ZhxmZ" : "_6Apj84DodnhHXzs23taUK1Q5Xg4fNyhmsu00eKk0T3",
    "j5WZuQHe05iNz81ZhxmZ" : "Qm0g/vv0pGZKaOXOkNL73o4/-lMW3xVwFRDh9px8WRU",
    "j5WZuQHe05yNz81ZhxmZ" : "MXzDZsAazbswbZQrBO8dGk_8 Ox-85rwOi_akbXkytd",
    "j5WZuQHe05-Oz81ZhxmZ" : "Y95QY2ADl-Ma1JhiOO0xAW-iXXifoydMji4MIXdD6_q",
    "j5WZuQHe05SOz81ZhxmZ" : "4WKyk6O_ -I5m_HIlmz_sWs5TS6rivrirGt/SmQreXh",
    "Mmbl5-d4RnL081ZhxmZ" : "ovz j4Q1GiLLxdVqoPWohve60Nr/3Lwqba0yYxPkQ/0",
    "j5WZuQHe05-M081ZhxmZ" : "A/51-ZUiV5Rr-XXFWWmQVunUYp2FI26GWa5goTBnufo",
    "j5WZuQHe05SM081ZhxmZ" : "0-mzzX-WGHYXJ1Jzu1ZViOR/Z6coGsGIG 1RscRuy2j",
    "j5WZuQHe05iM081ZhxmZ" : "0LrHb8yls--qBcHxx6In3-nT7-0zDJYHtRZ8yQbYms4",
    "j5WZuQHe05yM081ZhxmZ" : "IuuPZrbgKeL k6lHIBep7njjinpKa_Of-yuDoGAb8f0",
    "j5WZuQHe05-N081ZhxmZ" : "kXt8cBp/yuR /000Y3McIOXuMV4/F73ODpsYFtBi96i",
    "j5WZuQHe05SN081ZhxmZ" : "YjluSk8L5xvmivpWb-LR2YHt_8dSh8M3TB7ps-UIh6Q",
    "j5WZuQHe05iN081ZhxmZ" : "YZH5Zwm57hf3GZcSDZgwg-wthUzJpGImB1wRH97B2h1",
    "j5WZuQHe05yN081ZhxmZ" : "gD4JPXlJJ0NqSiG57 p/opBLBPj1wk51SV8NNQozPha",
    "j5WZuQHe05-O081ZhxmZ" : "snlwDu_2oZ1nJvV4SUzrjjNwnX_p0USQDFSAP7HviKZ",
    "j5WZuQHe05SO081ZhxmZ" : "454DgPfVhcb3pJpjLjxfAxtUHhngRGrvTYrzwM8m_1Y",
    "Mmbl5-d4RnL181ZhxmZ" : "sWpGT6d6xXQxdV2ZASbUUiMOgeKUyGJkzMHwsQNM-7T",
    "j5WZuQHe05-M181ZhxmZ" : "_k mQ1N HjeVRVVmHHy0IBs0bHsRbI_MLLJLKcjjZs4",
    "j5WZuQHe05SM181ZhxmZ" : "0sgM4yYBHYckscKzzgnkIQGVjXvS-5TeQ31YixBK1S1",
    "j5WZuQHe05iM181ZhxmZ" : "0D10/t/sx2ubSLesvfBpBHQ3IzANTKt36Gpza4gL175",
    "j5WZuQHe05yM181ZhxmZ" : "IvBGSaSNtyMb-dZMaKkbGAmuhMHMnTtctxgRjRORKy8",
    "j5WZuQHe05-N181ZhxmZ" : "cFDmohU81k2dQZRTh-WAhqU5KTfw2my0OdTI7v8sw2l",
    "j5WZuQHe05SN181ZhxmZ" : "U2Ny2Z2l8O6ydHHRc55wfksWP6K7wc0fagggW92zPYO",
    "j5WZuQHe05iN181ZhxmZ" : "4S4/i/2trkTDuaiZu6mMHDcxo T/ixX08oSLRtqo/an",
    "j5WZuQHe05yN181ZhxmZ" : "I-Nygh527T JZxrf3D1cciQtpttih6S59QB9w1_t02e",
    "j5WZuQHe05-O181ZhxmZ" : "IKu3_m5xI0ASe6efLJDOyHeKRf6NjnVVIi0/9FeOBeI",
    "j5WZuQHe05SO181ZhxmZ" : "gFcuLzU5jQwJBmAoUqDyTMO/7FO24dRLGbF4TsLgmKw",
    "Mmbl5-d4RnL281ZhxmZ" : "0h7yIaG-lmzfeSHpF/caBFusl8KRGnPLuYvWw4_o-zL",
    "Mmbl5-d4RnL381ZhxmZ" : "IZlAZWhTVPnUB3yr9D11 JGlTNmIAYkg16bXjc_BWzs",
    "Mmbl5-d4RnL481ZhxmZ" : "Mzmqd n3r0Vz/TpoaWHGLDcKndIzd9r-Oqw1t4TFcw7",
    "Mmbl5-d4RnL581ZhxmZ" : "kUfLVO1h2r1R7c_a0A8lTDh1Q g6KovyM5RtRVPd/Og",
}
for item, pay in data.items():
    ind = base64.b64decode(decodeb64(item)).decode('utf-8').replace("flag_", "").replace(".txt.enc", "")
    dat1 = decodeb64(data[item])
    flag[ind] = decrypt(dat1.replace(" ", "+"), "YaMfem0zr4jdiZsDUxv1TH69")
print("And here is your fucking flag: ")
for key in sorted(flag, key=int):
    print(flag[key], end="")