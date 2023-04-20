using Tele2App.Current;
using Tele2App.Services;

namespace Tele2App.View;

public partial class MainPage : ContentPage
{
    PointsService _service;
	public MainPage()
	{
		InitializeComponent();
        _service = new PointsService();
	}
    protected override bool OnBackButtonPressed()
    {
        return true;
    }
    protected async override void OnNavigatedTo(NavigatedToEventArgs args)
    {
        var current = CurrentUser.GetUser();
        VM.Notify(nameof(CurrentUser));
        await _service.UpdatePoints(new UpdatedUser()
        {
            Id = current.Id,
            Points = current.Points
        });
        base.OnNavigatedTo(args);
    }
}