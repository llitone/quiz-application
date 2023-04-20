using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Current;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    class AddRoom
    {
        public class SettingsViewModel : BaseViewModel
        {
            public ButtonCommand AddRoomCommand
            {
                get
                {
                    return new ButtonCommand(async () =>
                    {
                        await Shell.Current.GoToAsync(nameof(AddRoom));
                    });
                }
            }
        }
    }
}
