from django.urls import reverse, resolve

# Tests
class TestUrls:

    # Test Insert page
    def test_insert_url(self):
        path = reverse('insert')
        assert resolve(path).view_name == 'insert'

    # Test show page
    def test_show_url(self):
        path = reverse('show')
        assert resolve(path).view_name == 'show'

    # Test Salary page
    def test_salary_url(self):
        path = reverse('salary')
        assert resolve(path).view_name == 'salary'

    # Test Search page
    def test_search_url(self):
        path = reverse('search')
        assert resolve(path).view_name == 'search'

    # Test Delete page
    def test_delete_url(self):
        path = reverse('delete',kwargs={'id':1})
        assert resolve(path).view_name == 'delete'
    
    # Test Update page
    def test_update_url(self):
        path = reverse('update',kwargs={'id':1})
        assert resolve(path).view_name == 'update'