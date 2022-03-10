from accounts.forms import UserSearchForm


def search_form(request):
    return {'search_form': UserSearchForm(request.GET)}
