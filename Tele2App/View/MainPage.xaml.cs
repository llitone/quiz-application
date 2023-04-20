using Tele2App.Current;

namespace Tele2App.View;

public partial class MainPage : ContentPage
{
	public MainPage()
	{
		InitializeComponent();
	}
    protected override bool OnBackButtonPressed()
    {
        return true;
    }
    protected override void OnNavigatedTo(NavigatedToEventArgs args)
    {
        VM.Notify(nameof(CurrentUser));
        base.OnNavigatedTo(args);
    }
}