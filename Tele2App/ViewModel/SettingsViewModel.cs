using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Current;
using Tele2App.Services;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class SettingsViewModel : BaseViewModel
    {
        public ButtonCommand Logout
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    CurrentUser.Logout();
                    await Shell.Current.GoToAsync(nameof(LoginPage));
                });
            }
        }
    }
}
