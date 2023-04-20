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
}