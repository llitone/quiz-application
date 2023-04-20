using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.PortableExecutable;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;
using Tele2App.View;

namespace Tele2App.ViewModel;

public class RoomsViewModel : BaseViewModel
{
    private string _nameroom;

    public string NameRoom
    {
        get { return (_nameroom); }
        set
        {
            _nameroom = value;
            Notify(nameof(NameRoom));
        }
    }

    public ButtonCommand CreateRoom
    {
        get
        {
            return new ButtonCommand(async () =>
            {
                await Shell.Current.GoToAsync(nameof(RoomsPage));
            });
        }
    }
    public ButtonCommand AddRoom
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    await Shell.Current.GoToAsync(nameof(AddRoomPage));
                });
            }
        }
}
