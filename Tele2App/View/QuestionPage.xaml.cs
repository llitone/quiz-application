using Tele2App.Model;
using Tele2App.ViewModel;

namespace Tele2App.View;

public partial class QuestionPage : ContentPage
{
	public QuestionPage(Question question)
	{
		InitializeComponent();
		BindingContext = new QuestionViewModel(question);
	}
}