using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class LoginViewModel : BaseViewModel
    {
        public ButtonCommand Registration
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    await Shell.Current.GoToAsync(nameof(RegistrationPage));
                });
            }
        }
    }
}
