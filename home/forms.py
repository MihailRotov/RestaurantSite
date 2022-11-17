from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше імя', 'class': 'form'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-Mail', 'class': 'form'}
        )
    )

    subject = forms.CharField(
        min_length=5,
        max_length=40,
        widget=forms.TextInput(
            attrs={'placeholder': 'Тема звернення', 'class': 'form'}
        )
    )

    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Повідомлення: ', 'class': 'form textarea'}
        )
    )
