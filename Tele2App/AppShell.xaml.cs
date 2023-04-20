using Tele2App.View;

namespace Tele2App;

public partial class AppShell : Shell
{
	public AppShell()
	{
		InitializeComponent();
		Routing.RegisterRoute(nameof(LoginPage), typeof(LoginPage));
		Routing.RegisterRoute(nameof(RegistrationPage), typeof(RegistrationPage));
		Routing.RegisterRoute(nameof(MainPage), typeof(MainPage));
		Routing.RegisterRoute(nameof(SettingsPage), typeof(SettingsPage));
		Routing.RegisterRoute(nameof(RoomsPage), typeof(RoomsPage));
		Routing.RegisterRoute(nameof(AddRoomPage), typeof(AddRoomPage));
		Routing.RegisterRoute(nameof(QuestionPage), typeof(QuestionPage));
	}
}
