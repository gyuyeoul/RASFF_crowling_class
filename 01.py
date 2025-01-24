from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np
import csv
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import os
import warnings

os.environ["NLS_LANG"] = ".UTF8"
warnings.filterwarnings("ignore")


class crowling_rasff_details:
    def __init__(self, page_number, data_path, rasff_part):
        self.page_number = page_number
        self.data_path = data_path
        self.rasff_part = list(rasff_part)

    def rasff(self, page_number):
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        url = "https://webgate.ec.europa.eu/rasff-window/screen/search"
        options = webdriver.ChromeOptions()
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        )
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.implicitly_wait(3)
        driver.maximize_window()
        time.sleep(20)
        null = ""
        self.search_button = driver.find_element(
            By.XPATH, '//*[@id="search"]/div[3]/div[4]/button'
        ).click()
        page_number = self.page_number

        for u in range(page_number):
            for p in range(1, 26):  # items per page
                try:
                    self.details = driver.find_element(
                        By.XPATH,
                        f"/html/body/app-root/eui-app/div/div/app-search-component/div/app-list-component/div/div[2]/div[2]/div/app-nt-list-item[{p}]/div/div[10]/a",
                    ).click()
                except:
                    time.sleep(50)
                    self.details = driver.find_element(
                        By.XPATH,
                        f"/html/body/app-root/eui-app/div/div/app-search-component/div/app-list-component/div/div[2]/div[2]/div/app-nt-list-item[{p}]/div/div[10]/a",
                    ).click()

                driver.switch_to.window(driver.window_handles[1])

                try:
                    Reference = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[1]/div/p/span',
                    ).text
                except:
                    time.sleep(50)
                    Reference = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[1]/div/p/span',
                    ).text

                if "subject" in self.rasff_part:
                    # Subject

                    Subject = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[2]/div/p/span',
                    ).text
                    Notification_type = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[3]/div/p/span',
                    ).text
                    Notification_basis = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[4]/div/p/span',
                    ).text
                    Classification = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[5]/div/p/span',
                    ).text
                    Risk_decision = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[6]/div/p/span',
                    ).text

                    RASFF_Subject = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "SUBJECT",
                            "NOTIFICATION_TYPE",
                            "NOTIFICATION_BASIS",
                            "CLASSIFICATION",
                            "RISK_DECISION",
                        ]
                    )

                    RASFF_Subject = pd.concat(
                        [
                            RASFF_Subject,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "SUBJECT": [Subject],
                                    "NOTIFICATION_TYPE": [Notification_type],
                                    "NOTIFICATION_BASIS": [Notification_basis],
                                    "CLASSIFICATION": [Classification],
                                    "RISK_DECISION": [Risk_decision],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Subject = f"RASFF_Subject_{current_time}_by_Hwang.xlsx"
                    RASFF_Subject.to_excel(filename_Subject)

                else:
                    pass

                if "risk" in self.rasff_part:
                    RASFF_Risk = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "RISK_DECISION",
                            "HAZARDS_OBSERVED",
                            "NB_PERSONS_AFFENTED",
                            "SYMPTOMS_ILLNESS",
                        ]
                    )

                    Risk_decision = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[1]/app-nt-item[6]/div/p/span',
                    ).text
                    Hazards_observed = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-additional"]/div[1]/app-nt-item[2]/div/p/span',
                    ).text
                    Nb_persons_affected = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-additional"]/div[1]/app-nt-item[3]/div/p/span',
                    ).text
                    Symptoms_Illness = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-additional"]/div[1]/app-nt-item[4]/div/p/span',
                    ).text

                    RASFF_Risk = pd.concat(
                        [
                            RASFF_Risk,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "RISK_DECISION": [Risk_decision],
                                    "HAZARDS_OBSERVED": [Hazards_observed],
                                    "NB_PERSONS_AFFENTED": [Nb_persons_affected],
                                    "SYMPTOMS_ILLNESS": [Symptoms_Illness],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Risk = f"RASFF_Risk_{current_time}_by_Hwang.xlsx"
                    RASFF_Risk.to_excel(filename_Risk)

                else:
                    pass

                if "organisations" in self.rasff_part:
                    RASFF_Organisations = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "DATE_OF_NOTIFICATION",
                            "NOTIFYING",
                            "ORIGIN",
                            "DISTRIBUTION",
                            "OPERATOR",
                            "FLAGGED_FOR_FOLLOW_UP",
                            "FLAGGED_FOR_ATTENTION",
                        ]
                    )
                    Date_of_notification = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[3]/app-nt-item[1]/div/p/span',
                    ).text
                    Notifying = driver.find_element(
                        By.XPATH,
                        '//*[@id="main-info"]/div[3]/app-nt-item[2]/div/p/span',
                    ).text

                    try:

                        origin = driver.find_elements(
                            By.XPATH, "//app-country[contains(text(),'(o)')]"
                        )
                        origin_list = []
                        for j in origin:

                            a = j.text.replace("(n)", "")
                            a = a.replace("(o)", "")
                            a = a.replace("(d)", "")
                            a = a.replace("(op)", "")
                            a = a.replace("(ffup)", "")
                            a = a.replace("(ffa)", "")

                            origin_list.append(a)
                        origin_list = ", ".join(origin_list)
                    except NoSuchElementException:
                        origin_list = null

                    try:

                        distribution = driver.find_elements(
                            By.XPATH, " //app-country[contains(text(),'(d)')]"
                        )
                        distribution_list = []
                        for j in distribution:

                            a = j.text.replace("(n)", "")
                            a = a.replace("(o)", "")
                            a = a.replace("(d)", "")
                            a = a.replace("(op)", "")
                            a = a.replace("(ffup)", "")
                            a = a.replace("(ffa)", "")
                            distribution_list.append(a)
                        distribution_list = ", ".join(distribution_list)
                    except NoSuchElementException:
                        distribution_list = null

                    try:

                        operater = driver.find_elements(
                            By.XPATH, "//app-country[contains(text(),'(op)')]"
                        )
                        operater_list = []
                        for j in operater:
                            a = j.text.replace("(n)", "")
                            a = a.replace("(o)", "")
                            a = a.replace("(d)", "")
                            a = a.replace("(op)", "")
                            a = a.replace("(ffup)", "")
                            a = a.replace("(ffa)", "")
                            operater_list.append(a)
                        operater_list = ", ".join(operater_list)
                    except NoSuchElementException:
                        operater_list = null

                    try:

                        for_follow_up = driver.find_elements(
                            By.XPATH, "//app-country[contains(text(),'(ffup)')]"
                        )
                        for_follow_up_list = []
                        for j in for_follow_up:
                            a = j.text.replace("(n)", "")
                            a = a.replace("(o)", "")
                            a = a.replace("(d)", "")
                            a = a.replace("(op)", "")
                            a = a.replace("(ffup)", "")
                            a = a.replace("(ffa)", "")
                            for_follow_up_list.append(a)
                        for_follow_up_list = ", ".join(for_follow_up_list)

                    except NoSuchElementException:
                        for_follow_up_list = null

                    try:

                        for_attention = driver.find_elements(
                            By.XPATH, "//app-country[contains(text(),'(ffa)')]"
                        )
                        for_attention_list = []
                        for j in for_attention:
                            a = j.text.replace("(n)", "")
                            a = a.replace("(o)", "")
                            a = a.replace("(d)", "")
                            a = a.replace("(op)", "")
                            a = a.replace("(ffup)", "")
                            a = a.replace("(ffa)", "")
                            for_attention_list.append(a)
                        for_attention_list = ", ".join(for_attention_list)
                    except NoSuchElementException:
                        for_attention_list = null

                    RASFF_Organisations = pd.concat(
                        [
                            RASFF_Organisations,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "DATE_OF_NOTIFICATION": [Date_of_notification],
                                    "NOTIFYING": [Notifying],
                                    "ORIGIN": [origin_list],
                                    "DISTRIBUTION": [distribution_list],
                                    "OPERATOR": [operater_list],
                                    "FLAGGED_FOR_FOLLOW_UP": [for_follow_up_list],
                                    "FLAGGED_FOR_ATTENTION": [for_attention_list],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Organisations = (
                        f"RASFF_Organisation_{current_time}_by_Hwang.xlsx"
                    )
                    RASFF_Organisations.to_excel(filename_Organisations)
                else:
                    pass

                if "measure taken" in self.rasff_part:
                    RASFF_Measures_taken = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "COUNTRY",
                            "ACTION_RA",
                            "PRODUCT_NAME",
                            "URL",
                        ]
                    )
                    try:
                        Measures_taken = driver.find_element(
                            By.XPATH,
                            '//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody',
                        )
                        try:
                            number_Measures_taken = driver.find_elements(
                                By.CSS_SELECTOR,
                                "#main-additional > div.col-xl-6.col-lg-6.col-md-6.col-sm-12.col-12.col-print-12.measures-table > div > app-measures-table > div > table > tbody > tr",
                            )
                            country_text = []
                            action_text = []
                            product_name_text = []
                            url_text = []

                            for i in range(1, len(number_Measures_taken) + 1):
                                country = Measures_taken.find_element(
                                    By.XPATH,
                                    f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{i}]/td[1]/app-country',
                                )
                                action = Measures_taken.find_element(
                                    By.XPATH,
                                    f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{i}]/td[2]',
                                )
                                product_name = Measures_taken.find_element(
                                    By.XPATH,
                                    f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{i}]/td[3]',
                                )
                                url = Measures_taken.find_element(
                                    By.XPATH,
                                    f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{i}]/td[4]',
                                )
                                country_text.append(country.text)
                                action_text.append(action.text)
                                product_name_text.append(product_name.text)
                                url_text.append(url.text)
                            while len(number_Measures_taken) > 10:
                                if len(number_Measures_taken) <= 10:
                                    break

                                self.next_button_measures_taken = driver.find_element(
                                    By.XPATH,
                                    '//*[@id="main-additional"]/div[2]/div/app-measures-table/div/eui-paginator/div[2]/div[3]',
                                ).click()

                                number_Measures_taken = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#main-additional > div.col-xl-6.col-lg-6.col-md-6.col-sm-12.col-12.col-print-12.measures-table > div > app-measures-table > div > table > tbody > tr",
                                )

                                for k in range(1, len(number_Measures_taken) + 1):
                                    country = Measures_taken.find_element(
                                        By.XPATH,
                                        f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{k}]/td[1]/app-country',
                                    )
                                    action = Measures_taken.find_element(
                                        By.XPATH,
                                        f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{k}]/td[2]',
                                    )
                                    product_name = Measures_taken.find_element(
                                        By.XPATH,
                                        f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{k}]/td[3]',
                                    )
                                    url = Measures_taken.find_element(
                                        By.XPATH,
                                        f'//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr[{k}]/td[4]',
                                    )
                                    country_text.append(country.text)
                                    action_text.append(action.text)
                                    product_name_text.append(product_name.text)
                                    url_text.append(url.text)

                            country_text = ", ".join(country_text)
                            action_text = ", ".join(action_text)
                            product_name_text = ", ".join(product_name_text)
                            url_text = ", ".join(url_text)
                        except:
                            country_text = Measures_taken.find_element(
                                By.XPATH,
                                '//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr/td[1]/app-country',
                            ).text
                            action_text = Measures_taken.find_element(
                                By.XPATH,
                                '//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr/td[2]',
                            ).text
                            product_name_text = Measures_taken.find_element(
                                By.XPATH,
                                '//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr/td[3]',
                            ).text
                            url_text = Measures_taken.find_element(
                                By.XPATH,
                                '//*[@id="main-additional"]/div[2]/div/app-measures-table/div/table/tbody/tr/td[4]',
                            ).text

                    except NoSuchElementException:
                        country_text = null
                        action_text = null
                        product_name_text = null
                        url_text = null

                    RASFF_Measures_taken = pd.concat(
                        [
                            RASFF_Measures_taken,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "COUNTRY": [country_text],
                                    "ACTION": [action_text],
                                    "PRODUCT_NAME": [product_name_text],
                                    "URL": [url_text],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Measures_taken = (
                        f"RASFF_Measures_taken_{current_time}_by_Hwang.xlsx"
                    )
                    RASFF_Measures_taken.to_excel(filename_Measures_taken)
                else:
                    pass

                if "follow ups" in self.rasff_part:
                    RASFF_Follow_ups = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "FUP",
                            "DATE_RA",
                            "ORGANISATION",
                            "TYPE_RA",
                            "SUMMARY",
                            "FLAGGED_ORGANISATIONS",
                        ]
                    )
                    try:
                        follow_ups = driver.find_element(
                            By.XPATH,
                            '//*[@id="followups"]/div/div/app-followups-table/table/tbody',
                        )
                        try:
                            number_follow_ups = driver.find_elements(
                                By.CSS_SELECTOR,
                                "#followups > div > div > app-followups-table > table > tbody > tr",
                            )
                            # Follow-ups
                            fup_text = []
                            date_text = []
                            organisation_text = []
                            type__text = []
                            summary_text = []
                            for i in range(1, len(number_follow_ups) + 1):
                                fup = follow_ups.find_element(
                                    By.XPATH,
                                    f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[1]',
                                )
                                date = follow_ups.find_element(
                                    By.XPATH,
                                    f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[2]/span',
                                )
                                organisation = follow_ups.find_element(
                                    By.XPATH,
                                    f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[3]/span',
                                )
                                type_ = follow_ups.find_element(
                                    By.XPATH,
                                    f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[4]',
                                )
                                summary = follow_ups.find_element(
                                    By.XPATH,
                                    f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[5]',
                                )
                                fup_text.append(fup.text)
                                date_text.append(date.text)
                                organisation_text.append(organisation.text)
                                type__text.append(type_.text)
                                summary_text.append(summary.text)

                            while len(number_follow_ups) > 10:
                                if len(number_follow_ups) <= 10:
                                    break

                                self.next_button_follow_ups = driver.find_element(
                                    By.XPATH,
                                    '//*[@id="followups"]/div/div/app-followups-table/eui-paginator/div[2]/div[3]',
                                ).click
                                number_follow_ups = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#followups > div > div > app-followups-table > table > tbody > tr",
                                )

                                for i in range(1, len(number_follow_ups) + 1):
                                    fup = follow_ups.find_element(
                                        By.XPATH,
                                        f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[1]',
                                    )
                                    date = follow_ups.find_element(
                                        By.XPATH,
                                        f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[2]/span',
                                    )
                                    organisation = follow_ups.find_element(
                                        By.XPATH,
                                        f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[3]/span',
                                    )
                                    type_ = follow_ups.find_element(
                                        By.XPATH,
                                        f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[4]',
                                    )
                                    summary = follow_ups.find_element(
                                        By.XPATH,
                                        f'//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr[{i}]/td[5]',
                                    )

                                    fup_text.append(fup.text)
                                    date_text.append(date.text)
                                    organisation_text.append(organisation.text)
                                    type__text.append(type_.text)
                                    summary_text.append(summary.text)

                            flagged_organisations = (
                                fup_text[len(number_follow_ups)] + for_follow_up_list
                            )
                            fup_text = ", ".join(fup_text)
                            date_text = ", ".join(date_text)
                            organisation_text = ", ".join(organisation_text)
                            type_text = ", ".join(type_text)
                            summary_text = ", ".join(summary_text)

                        except:
                            fup_text = follow_ups.find_element(
                                By.XPATH,
                                '//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr/td[1]',
                            ).text
                            date_text = follow_ups.find_element(
                                By.XPATH,
                                '//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr/td[2]/span',
                            ).text
                            organisation_text = follow_ups.find_element(
                                By.XPATH,
                                '//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr/td[3]/span',
                            ).text
                            type__text = follow_ups.find_element(
                                By.XPATH,
                                '//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr/td[4]',
                            ).text
                            summary_text = follow_ups.find_element(
                                By.XPATH,
                                '//*[@id="followups"]/div/div/app-followups-table/table/tbody/tr/td[5]',
                            ).text
                            flagged_organisations = for_follow_up_list

                    except NoSuchElementException:
                        fup_text = null
                        date_text = null
                        organisation_text = null
                        type__text = null
                        summary_text = null
                        flagged_organisations = null

                    RASFF_Follow_ups = pd.concat(
                        [
                            RASFF_Follow_ups,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "FUP": [fup_text],
                                    "DATE": [date_text],
                                    "ORGANISATION": [organisation_text],
                                    "TYPE": [type__text],
                                    "SUMMARY": [summary_text],
                                    "FLAGGED_ORGANISATIONS": [flagged_organisations],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Follow_ups = (
                        f"RASFF_Follow_ups_{current_time}_by_Hwang.xlsx"
                    )
                    RASFF_Follow_ups.to_excel(filename_Follow_ups)
                else:
                    pass

                if "products" in self.rasff_part:
                    RASFF_Products = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "CATEGORY",
                            "NAME",
                            "DISTRIBUTION_STATUS",
                            "HAZARD",
                            "MEASURES_TAKEN",
                        ]
                    )
                    try:
                        products = driver.find_element(
                            By.XPATH,
                            '//*[@id="products"]/div/div/app-products-table/table/tbody',
                        )
                        try:
                            number_products = driver.find_elements(
                                By.CLASS_NAME,
                                "#products > div > div > app-products-table > table > tbody > tr",
                            )
                            category_text = []
                            name_text = []
                            distribution_status_text = []

                            for i in range(1, len(number_products) + 1):
                                category = products.find_element(
                                    By.XPATH,
                                    f'//*[@id="products"]/div/div/app-products-table/table/tbody/tr[{i}]/td[2]',
                                )
                                name = products.find_element(
                                    By.XPATH,
                                    f'//*[@id="products"]/div/div/app-products-table/table/tbody/tr[{i}]/td[3]',
                                )
                                distribution_status = products.find_element(
                                    By.XPATH,
                                    f'//*[@id="products"]/div/div/app-products-table/table/tbody/tr[{i}]/td[4]',
                                )

                                category_text.append(category.text)
                                name_text.append(name.text)
                                distribution_status_text.append(
                                    distribution_status.text
                                )

                            while len(number_products) > 10:
                                if len(number_products) <= 10:
                                    break
                                self.next_button_number_products = driver.find_element(
                                    By.XPATH,
                                    '//*[@id="products"]/div/div/app-products-table/eui-paginator/div[2]/div[3]',
                                ).click()
                                number_products = driver.find_elements(
                                    By.CLASS_NAME,
                                    "#products > div > div > app-products-table > table > tbody > tr",
                                )

                                for i in range(1, len(number_products) + 1):
                                    category = products.find_element(
                                        By.XPATH,
                                        f'//*[@id="products"]/div/div/app-products-table/table/tbody/tr[{i}]/td[2]',
                                    )
                                    name = products.find_element(
                                        By.XPATH,
                                        f'//*[@id="products"]/div/div/app-products-table/table/tbody/tr[{i}]/td[3]',
                                    )
                                    distribution_status = products.find_element(
                                        By.XPATH,
                                        f'//*[@id="products"]/div/div/app-products-table/table/tbody/tr[{i}]/td[4]',
                                    )

                                    category_text.append(category.text)
                                    name_text.append(name.text)
                                    distribution_status_text.append(
                                        distribution_status.text
                                    )
                            category_text = ", ".join(category_text)
                            name_text = ", ".join(name_text)
                            distribution_status_text = ", ".join(
                                distribution_status_text
                            )

                        except:
                            category_text = products.find_element(
                                By.XPATH,
                                '//*[@id="products"]/div/div/app-products-table/table/tbody/tr/td[2]',
                            ).text
                            name_text = products.find_element(
                                By.XPATH,
                                '//*[@id="products"]/div/div/app-products-table/table/tbody/tr/td[3]',
                            ).text
                            distribution_status_text = products.find_element(
                                By.XPATH,
                                '//*[@id="products"]/div/div/app-products-table/table/tbody/tr/td[4]',
                            ).text

                    except NoSuchElementException:
                        category_text = null
                        name_text = null
                        distribution_status_text = null
                        hazard_text = null

                    RASFF_Products = pd.concat(
                        [
                            RASFF_Products,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "CATEGORY": [category_text],
                                    "NAME": [name_text],
                                    "DISTRIBUTION_STATUS": [distribution_status_text],
                                    "HAZARD": [hazard_text],
                                    "MEASURES_TAKEN": [action_text],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Products = f"RASFF_Products_{current_time}_by_Hwang.xlsx"
                    RASFF_Products.to_excel(filename_Products)
                else:
                    pass

                if "hazards" in self.rasff_part:
                    RASFF_Hazards = pd.DataFrame(
                        columns=[
                            "REFERENCE",
                            "SAMPLING",
                            "HAZARD",
                            "CATEGORY",
                            "ANALYTICAL_RESULTS",
                            "MAXIMUM",
                        ]
                    )
                    try:
                        Hazards = driver.find_element(
                            By.XPATH,
                            '//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody',
                        )
                        try:
                            number_Hazards = driver.find_elements(
                                By.CSS_SELECTOR,
                                "#hazards > div > div > app-hazards-table > div > table > tbody > tr",
                            )

                            sampling_text = []
                            hazard_text = []
                            hazards_category_text = []
                            analytical_results_text = []
                            maximum_text = []

                            for i in range(1, len(number_Hazards) + 1):
                                sampling = Hazards.find_element(
                                    By.XPATH,
                                    f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[1]',
                                )
                                hazard = Hazards.find_element(
                                    By.XPATH,
                                    f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[2]/strong',
                                )
                                hazards_category = Hazards.find_element(
                                    By.XPATH,
                                    f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[3]',
                                )
                                analytical_results = Hazards.find_element(
                                    By.XPATH,
                                    f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[4]',
                                )
                                maximum = Hazards.find_element(
                                    By.XPATH,
                                    f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[5]',
                                )

                                sampling_text.append(sampling.text)
                                hazard_text.append(hazard.text)
                                hazards_category_text.append(hazards_category.text)
                                analytical_results_text.append(analytical_results.text)
                                maximum_text.append(maximum.text)

                            while len(number_Hazards) > 10:
                                if len(number_Hazards) <= 10:
                                    break
                                self.next_button_Hazards = driver.find_element(
                                    By.XPATH,
                                    '//*[@id="hazards"]/div/div/app-hazards-table/div/eui-paginator/div[2]/div[3]/button',
                                ).click()
                                number_Hazards = driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "#hazards > div > div > app-hazards-table > div > table > tbody > tr",
                                )

                                for i in range(1, len(number_Hazards) + 1):
                                    sampling = Hazards.find_element(
                                        By.XPATH,
                                        f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[1]',
                                    )
                                    hazard = Hazards.find_element(
                                        By.XPATH,
                                        f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[2]/strong',
                                    )
                                    hazards_category = Hazards.find_element(
                                        By.XPATH,
                                        f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[3]',
                                    )
                                    analytical_results = Hazards.find_element(
                                        By.XPATH,
                                        f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[4]',
                                    )
                                    maximum = Hazards.find_element(
                                        By.XPATH,
                                        f'//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr[{i}]/td[5]',
                                    )

                                    sampling_text.append(sampling.text)
                                    hazard_text.append(hazard.text)
                                    hazards_category_text.append(hazards_category.text)
                                    analytical_results_text.append(
                                        analytical_results.text
                                    )
                                    maximum_text.append(maximum.text)

                            sampling_text = ", ".join(sampling_text)
                            hazard_text = ", ".join(hazard_text)
                            hazards_category_text = ", ".join(hazards_category_text)
                            analytical_results_text = ", ".join(analytical_results_text)
                            maximum_text = ", ".join(maximum_text)

                        except:
                            sampling_text = Hazards.find_element(
                                By.XPATH,
                                '//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr/td[1]/span',
                            ).text
                            hazard_text = Hazards.find_element(
                                By.XPATH,
                                '//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr/td[2]/strong',
                            ).text
                            hazards_category_text = Hazards.find_element(
                                By.XPATH,
                                '//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr/td[3]',
                            ).text
                            analytical_results_text = Hazards.find_element(
                                By.XPATH,
                                '//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr/td[4]',
                            ).text
                            maximum_text = Hazards.find_element(
                                By.XPATH,
                                '//*[@id="hazards"]/div/div/app-hazards-table/div/table/tbody/tr/td[5]',
                            ).text

                    except NoSuchElementException:

                        sampling_text = null
                        hazard_text = null
                        hazards_category_text = null
                        analytical_results_text = null
                        maximum_text = null

                    RASFF_Hazards = pd.concat(
                        [
                            RASFF_Hazards,
                            pd.DataFrame(
                                {
                                    "REFERENCE": [Reference],
                                    "SAMPLING": [sampling_text],
                                    "HAZARD": [hazard_text],
                                    "CATEGORY": [hazards_category_text],
                                    "ANALYTICAL_RESULTS": [analytical_results_text],
                                    "MAXIMUM": [maximum_text],
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    filename_Hazards = f"RASFF_Hazards_{current_time}_by_Hwang.xlsx"
                    RASFF_Hazards.to_excel(filename_Hazards)
                else:
                    pass
            if u != page_number:
                driver.find_element(
                    By.XPATH,
                    "/html/body/app-root/eui-app/div/div/app-search-component/div/app-list-component/div/div[3]/mat-paginator/div/div/div[2]/button[2]/span[3]",
                ).click()
            else:
                pass
