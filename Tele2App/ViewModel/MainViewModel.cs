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
        private SubjectsService _subjectsService;
        private EverydayTasksService _everydayTasksService;
        public CurrentUser CurrentUser { get; set; }

        public ObservableCollection<Question> EverydayTasks { get; set; }

        public MainViewModel()
        {
            CurrentUser = CurrentUser.GetUser();
            CurrentUser.Name = ConvertName(CurrentUser.Name);
            _subjectsService = new SubjectsService();
            _everydayTasksService = new EverydayTasksService();
            GetSubjectsAndSetEverydayTasks();
        }

        private string ConvertName(string name)
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

        private async void GetSubjectsAndSetEverydayTasks()
        {
            var data = await _subjectsService.GetSubjects();
            SubjectsData.SetSubjects(data);

            EverydayTasks = new ObservableCollection<Question>(_everydayTasksService.GetTasks(10));
            Notify(nameof(EverydayTasks));  
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

        public ButtonCommand OpenExchange
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    await Shell.Current.GoToAsync(nameof(ExchangePage));
                });
            }
        }

        public ButtonCommandWithParameter GoToQuestion
        {
            get
            {
                return new ButtonCommandWithParameter(async (Question) =>
                {
                    if (Question is null)
                        return;

                    await Shell.Current.Navigation.PushAsync(new QuestionPage(Question as Question));
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
