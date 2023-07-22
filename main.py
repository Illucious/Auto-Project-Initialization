from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
import time
from os import system, chdir

reponame = input("Enter the repo name you want to create: ")
username = "Your email address here"
password = "Your github password here"
projectfolder_path = r"path to projects folder here"


def github_setup(username=username, password=password, reponame=reponame):
    service = Service(executable_path="chromedriver")
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://github.com/")

    signIn = driver.find_element(By.LINK_TEXT, "Sign in")
    signIn.click()

    time.sleep(2)

    username_field = driver.find_element(By.ID, "login_field")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    signInButton = driver.find_element(By.CLASS_NAME, "js-sign-in-button")
    signInButton.click()

    time.sleep(2)

    newRepo_button = driver.find_element(By.CLASS_NAME, "Button--primary")
    newRepo_button.click()

    time.sleep(2)

    repoName_field = driver.find_element(By.ID, "react-aria-2")
    repoName_field.send_keys(reponame)

    time.sleep(2)

    createRepo_button = driver.find_element(By.CLASS_NAME, "bZiiSx")
    createRepo_button.click()

    time.sleep(5)

    github_url = driver.current_url
    return github_url


def main(reponame=reponame, projectfolderpath=projectfolder_path):
    projects_folder_path = projectfolderpath

    system("echo welcome")
    chdir(projects_folder_path)
    system(f'mkdir "{reponame}"')
    chdir(projectfolderpath + "/" + f"{reponame}")
    system("git init")
    system("call>README.md")
    system("git add . ")
    system('git commit -m "Initial Commit" ')

    github_url = github_setup()
    print(github_url)

    chdir(projectfolderpath + "/" + f"{reponame}")
    system(f"git remote add origin {github_url}.git")
    system("git push --all --set-upstream origin")
    system("code .")
    print("congratulations!! Repo successfully created....")


main()
