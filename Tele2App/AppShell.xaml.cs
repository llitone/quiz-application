using Tele2App.View;

namespace Tele2App;

public partial class AppShell : Shell
{
	public AppShell()
	{
		InitializeComponent();
		Routing.RegisterRoute(nameof(LoginPage), typeof(LoginPage));
		Routing.RegisterRoute(nameof(RegistrationPage), typeof(RegistrationPage));
	}
}
