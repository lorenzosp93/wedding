from django.test import TestCase
from .models import ContentString, TranslatedString, get_translated_content

# Create your tests here.
class TestSharedContentModels(TestCase):
    """
    Class to test the `ContentString` module 
    """
    def setUp(self) -> None:
        "Provide initial values to tests"
        self.test_string = ContentString.objects.create(
            value="""
            <div>
                <h1>Test ContentString</h1>
                <p>This is a test ContentString with html content</p>
            </div>
            """
        )
        self.es_test_string = TranslatedString.objects.create(
            t9n="""
            <div>
                <h1>Prueba ContentString</h1>
                <p>Esta es una ContentString de prueba con contenido html</p>
            </div>
            """,
            language=2,
            content=self.test_string,
        )
        self.it_test_string = TranslatedString.objects.create(
            t9n="""
            <div>
                <h1>Prova ContentString</h1>
                <p>Questa è una ContentString di prova con contenuto html</p>
            </div>
            """,
            language=1,
            content=self.test_string,
        )
    
    def test_contentstring_creation(self) -> None:
        self.assertIsInstance(self.test_string, ContentString)
    
    def test_translatedstring_creation(self) -> None:
        self.assertIsInstance(self.es_test_string, TranslatedString)

    def get_translated_content(self) -> None:
        es_string = get_translated_content(self.test_string, 2)
        self.assertEqual(es_string, self.es_test_string.t9n)
