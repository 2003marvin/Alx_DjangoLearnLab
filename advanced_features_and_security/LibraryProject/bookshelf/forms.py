from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if "<script>" in title:  # Prevent XSS injection
            raise forms.ValidationError("Invalid title")
        return title


class ExampleForm(forms.Form):
    """A sample form to demonstrate secure form handling."""
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter a book title (max 100 characters)."
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text="Enter a brief description of the book."
    )

    def clean_title(self):
        """Validate title input to prevent XSS attacks."""
        title = self.cleaned_data['title']
        if "<script>" in title:  # Prevent script injection
            raise forms.ValidationError("Invalid title: potential XSS detected.")
        return title
