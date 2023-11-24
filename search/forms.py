from django import forms

class PostSearchForm(forms.Form): #사용자에게 검색어를 입력받음
    search_word = forms.CharField(label='Search Word')