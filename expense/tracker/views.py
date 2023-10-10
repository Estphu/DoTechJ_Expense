from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ProfileForm
from .models import Profile,Expense
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def homeview(request):
    profile = Profile.objects.filter(user=request.user).first()
    expenses = Expense.objects.filter(user=request.user)
    if(profile is None):
        return redirect('tracker:profile',id=request.user.id)
    else:
        if request.method == 'POST':
            text = request.POST.get('text')
            amount = request.POST.get('amount')
            expense_type = request.POST.get('expense_type')
            expense = Expense(name=text,amount=amount,expense_type=expense_type,user=request.user)
            expense.save()
            if(expense_type == 'Positive'):
                profile.balance += float(amount)
            else:
                profile.expense += float(amount)
                profile.balance -= float(amount)
            profile.save()       
            return redirect('/')
    context = {'profile':profile, 'expenses':expenses}
    return render(request, 'tracker/home.html',context=context)

class ProfileCreateView(CreateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        self.get_object = form.save(commit=False)
        self.get_object.user = self.request.user
        self.get_object.save()
        return super().form_valid(form)