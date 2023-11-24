from django.views.generic.edit import FormView #폼 관련
from django.db.models import Q #쿼리
from django.shortcuts import render #템플릿 렌더링
from search.forms import PostSearchForm 

# formView 구현
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    #검색어를 받고 검색하여 결과 보여줌
    def form_valid(self, form):
        schWord = self.request.POST['search_word']
        #검색 기능
        post_list = Post.objects.filter(
            Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)
        ).distinct()

        #결과값 반환 폼
        context = {
            'form': form,
            'search_term': schWord,
            'object_list': post_list,
        }

        #form_valid()함수는 리다이렉트 처리를 위해 HttpResponseRedirect객체를 반환하는데
        # #render()함수는 httpResponse객체를 반환하도록 도와준다.(리다이렉트 처리 되지 않도록)
        return render(self.request, self.template_name, context)