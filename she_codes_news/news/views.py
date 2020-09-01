from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        # return NewsStory.objects.all()
        return NewsStory.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all()[:4]
        # context['all_stories'] = NewsStory.objects.all()
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'editStory'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def edit_story(request,slug):
        story = Story.objects.get(slug=slug)
        if request.method == 'POST':
            form = forms.EditStory(request.POST, instance=story)
            if form.is_valid():
                form.save()
                return redirect('story:list')
        else:
            form = forms.EditArticle(instance=article)
        args = {'form': form}
        return render(request, 'news/editStory.html', args)