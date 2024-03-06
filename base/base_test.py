import pytest

from pages.sbis_index_page import SbisIndexPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_index_page import TensorIndexPage
from pages.tensor_about_page import TensorAboutPage
from pages.sbis_download_pages import SbisDownloadReportPage, SbisDownloadPluginPage


class BaseTest:

    sbis_index_page: SbisIndexPage
    sbis_contacts_page: SbisContactsPage
    sbis_download_report_page: SbisDownloadReportPage
    sbis_download_plugin_page: SbisDownloadPluginPage
    tensor_index_page: TensorIndexPage
    tensor_about_page: TensorAboutPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.sbis_index_page = SbisIndexPage(driver)
        request.cls.sbis_contacts_page = SbisContactsPage(driver)
        request.cls.sbis_download_report_page = SbisDownloadReportPage(driver)
        request.cls.sbis_download_plugin_page = SbisDownloadPluginPage(driver)
        request.cls.tensor_index_page = TensorIndexPage(driver)
        request.cls.tensor_about_page = TensorAboutPage(driver)