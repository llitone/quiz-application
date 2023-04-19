using System.ComponentModel;
using Tele2App.Current;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class MainViewModel : BaseViewModel
    {
        public CurrentUser CurrentUser { get; set; }

        public MainViewModel()
        {
            CurrentUser = CurrentUser.GetUser();
        }

        public ButtonCommand OpenSetting
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    await Shell.Current.GoToAsync(nameof(SettingsPage));
                });
            }
        }

        public ButtonCommand OpenRooms
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    await Shell.Current.GoToAsync(nameof(RoomsPage));
                });
            }
        }
    }
}
