from django.views.generic.edit import FormView #폼 관련
from django.db.models import Q #쿼리
from django.shortcuts import render #템플릿 렌더링
from search.forms import PostSearchForm 

# formView 구현
class SearchFormView(FormView):
    1번에서 만든 form객체를 form_class로 지정한다.

form_class = PostSearchForm 

​

사용할 템플릿

 template_name = 'blog/post_search.html'

​

검색어

schWord='%s' % self.request.POST['search_word']

​

검색의 핵심은 Q기능에 있다. 

post_list = Post.objects.filter( Q(title__icontains = schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord) ).distinct()

​

결과값 반환 form

 context={}

 context['form'] = form

 context['search_term'] = schWord

 context['object_list'] = post_list

​

form_valid()함수는 리다이렉트 처리를 위해 HttpResponseRedirect객체를 반환하는데..

render()함수는 httpResponse객체를 반환하도록 도와준다.(리다이렉트 처리 되지 않도록)

retrun render(self.request, self.template_name, context)