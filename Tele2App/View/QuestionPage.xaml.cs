using Tele2App.Model;
using Tele2App.ViewModel;

namespace Tele2App.View;

public partial class QuestionPage : ContentPage
{
    QuestionViewModel _viewModel;
    int _time = 10;
	IDispatcherTimer _timer;
	public QuestionPage(Question question)
	{
		InitializeComponent();
        _viewModel = new QuestionViewModel(question);
        BindingContext = _viewModel;
        _viewModel.StopTimer += _viewModel_StopTimer;
        _timer = Dispatcher.CreateTimer();
		_timer.Interval = new TimeSpan(0, 0, 1);
        _timer.Tick += _timer_Tick;
        _timer.Start();
    }

    private void _viewModel_StopTimer()
    {
        _timer.Stop();
    }

    private async void _timer_Tick(object sender, EventArgs e)
    {
        if(_time <= 0)
        {
            _timer.Stop();
            await Shell.Current.DisplayAlert(string.Empty, "Время вышло!", "На главную");
            await Shell.Current.GoToAsync(nameof(MainPage), true);
        }
        _time--;
        Time.Text = _time.ToString();
    }
    protected override bool OnBackButtonPressed()
    {
        return true;
    }
}