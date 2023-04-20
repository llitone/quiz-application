using System.Collections.ObjectModel;
using System.ComponentModel;
using Tele2App.Current;
using Tele2App.Data;
using Tele2App.Model;
using Tele2App.Services;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class MainViewModel : BaseViewModel
    {
        private SubjectsService _service;
        public CurrentUser CurrentUser { get; set; }

        public MainViewModel()
        {
            CurrentUser = CurrentUser.GetUser();
            _service = new SubjectsService();
            GetSubjects();
        }

        private async void GetSubjects()
        {
            var data = await _service.GetSubjects();
            SubjectsData.SetSubjects(data);
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
