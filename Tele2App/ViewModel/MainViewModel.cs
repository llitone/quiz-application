using System.ComponentModel;
using Tele2App.Current;

namespace Tele2App.ViewModel
{
    public class MainViewModel : BaseViewModel
    {
        public CurrentUser CurrentUser { get; set; }

        public MainViewModel()
        {
            CurrentUser = CurrentUser.GetUser();
        }
    }
}
