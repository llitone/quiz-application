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
            CurrentUser.Name = ConvertName(CurrentUser.Name);
        }
        private string _convert_name(string name)
        {
            string result = "";
            int count = 0;
            foreach (char ch in name)
            {
                if (count > 10)
                {
                    break;
                }
                result += ch;
                count++;
            }
            result += "...";
            return result;
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
