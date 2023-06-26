import requests
from bs4 import BeautifulSoup
from data import username, password
from pprint import pprint


def main():
    login_url = "https://www.dream-singles.com/login"
    target_url = "https://www.dream-singles.com/members/connections/myFavorites?all=1&folder=32483"

    with requests.session() as session:
        response = session.get(login_url)

        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find(id='_token').get('value')
        print(token)

        data = {
            '_username': username,
            '_password': password,
            '_token': token,
            "g-recaptcha-response": "03AL8dmw-VfNik2_fO3VpB2vEksNBfXwNiH4Cb6YmaBXiDJJjznlFcZ9cMEkoz_HY2n-YP60KkpWbctEZ3x0BlYDohFI9CUVd62LEILsndDsr4eJuUbWi5lZ4vnuFOcJkaA7G9PaHnNKCRzG8cLYlx5IPobjopl9S_qTGwudo3niUbVoWGagnla4ykg7cVIYzvAItO9xzDJGOpR0Wkqyf5Wq5U8BwWe2PuPxLR0MohVMUmWSDUKSjbeJilBys3Frnh7PyjPF7Ddr4RD6bP4qTFATO91GJrkBP73exQ69fIJb7qNE9C4tamyEvBstvIsjpLpAMqd3ECkLcBNnj1oSzyRJk1GM82HiRoJEF53li96D0zqQHfSOqlUE9QGo3lZnrro0ghKRjJiwQHkMyL6Al8n0ZJhSd2fXk9uysxW6sSuuQxw7E9DDyzEcAYsjTOWxiSLXeH1FnpSCRp8c7z7p09d_yRnz9OuctO9dzwybrSDRNQrzPi4XE-YsZ7DBIgX…XZNhcY_mboRK-NY3hXaACyB9Nhzg23zYqgOZuY-kIzknCYQWl5QBuvg_rhCjZ8GwlNZUjy958obnMywE5SPB2NZXtfr6iV9dbK_URrSUWtZATqfLJk73qfUTwtacI90dV8lxrjPat2dWXy3INg6SD4J3R_i2WdybCjdi9Gpttm0yn3JSwNUPIV37FnjEDj8XBRbOe8XT3JdMaQiYAAht0jI2sP-0kMqf3rwAuwRIuUtZqkogXjvNRy26VskHpAX7y5TN_wS4AYg0Si5qrb_2M-k0OGVFHhoJng_ULUG9rPLe8xJo9ynH-86hIDOjuMaEhe5A2FNPHsDd9Ak4d4p3NZz0LHFhqrDKKizLCmZl5UF59ZQcG55ipsUegGmnTrii4YZPSIi8WhobuUlHru3GKYvGD5Q0ijCEa6tWZMPtz5XD5gBvsjB4ZNeJkqR5szAFZY9JOMFyUCmqJ9R9merpB89FyCNWqGQo5fI-tltFR-5BUVoUrUZkW7WjUx506b"
        }

        r_post = session.post(login_url, data=data)

        pprint(r_post.text)
        with open('html/index.html', 'w', encoding='utf-8') as f:
            f.write(r_post.text)


# login_data = {
#     "_username": username,
#     "_password": password,
#     "_token": "5DKPC7Kro0c_0qvrZ6gf8Q48KjrSyjbDrzmc542Q08w",
#     "g-recaptcha-response": "03AL8dmw-VfNik2_fO3VpB2vEksNBfXwNiH4Cb6YmaBXiDJJjznlFcZ9cMEkoz_HY2n-YP60KkpWbctEZ3x0BlYDohFI9CUVd62LEILsndDsr4eJuUbWi5lZ4vnuFOcJkaA7G9PaHnNKCRzG8cLYlx5IPobjopl9S_qTGwudo3niUbVoWGagnla4ykg7cVIYzvAItO9xzDJGOpR0Wkqyf5Wq5U8BwWe2PuPxLR0MohVMUmWSDUKSjbeJilBys3Frnh7PyjPF7Ddr4RD6bP4qTFATO91GJrkBP73exQ69fIJb7qNE9C4tamyEvBstvIsjpLpAMqd3ECkLcBNnj1oSzyRJk1GM82HiRoJEF53li96D0zqQHfSOqlUE9QGo3lZnrro0ghKRjJiwQHkMyL6Al8n0ZJhSd2fXk9uysxW6sSuuQxw7E9DDyzEcAYsjTOWxiSLXeH1FnpSCRp8c7z7p09d_yRnz9OuctO9dzwybrSDRNQrzPi4XE-YsZ7DBIgX…XZNhcY_mboRK-NY3hXaACyB9Nhzg23zYqgOZuY-kIzknCYQWl5QBuvg_rhCjZ8GwlNZUjy958obnMywE5SPB2NZXtfr6iV9dbK_URrSUWtZATqfLJk73qfUTwtacI90dV8lxrjPat2dWXy3INg6SD4J3R_i2WdybCjdi9Gpttm0yn3JSwNUPIV37FnjEDj8XBRbOe8XT3JdMaQiYAAht0jI2sP-0kMqf3rwAuwRIuUtZqkogXjvNRy26VskHpAX7y5TN_wS4AYg0Si5qrb_2M-k0OGVFHhoJng_ULUG9rPLe8xJo9ynH-86hIDOjuMaEhe5A2FNPHsDd9Ak4d4p3NZz0LHFhqrDKKizLCmZl5UF59ZQcG55ipsUegGmnTrii4YZPSIi8WhobuUlHru3GKYvGD5Q0ijCEa6tWZMPtz5XD5gBvsjB4ZNeJkqR5szAFZY9JOMFyUCmqJ9R9merpB89FyCNWqGQo5fI-tltFR-5BUVoUrUZkW7WjUx506b"
# }


#
# session = requests.session()
# response = session.get(login_url)
#
# soup = BeautifulSoup(response.content, "html.parser")
# if 'login' in str(soup):
#     print('you are in log page')
# print(str(soup))
# response = session.post(login_url, data=login_data)
#
# if response.status_code == 200:
#     print("Login successful!")
# else:
#     print("Login failed!")
#
# response = session.get(target_url)

#
# # Check if the target page was accessed successfully
# if response.status_code == 200:
#     print("Accessed the target page successfully!")
# else:
#     print("Failed to access the target page!")
#
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
#
# if 'login' in str(soup):
#     print('you are in log page')
#
# button = None
# while True:
#     button = soup.find("a")
#     if "View his Messages" in button:
#         break


# link = button.get("href")

# print(button)
# print('-----------')
# print(link)

if __name__ == '__main__':
    main()
