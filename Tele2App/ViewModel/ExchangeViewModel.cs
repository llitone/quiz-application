using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tele2App.ViewModel
{
    public class ExchangeViewModel : BaseViewModel
    {
        public int Points { get; set; }
        public ExchangeViewModel()
        {
            Points = Current.CurrentUser.GetUser().Points;
            Notify(nameof(Points));
        }
    }
}
