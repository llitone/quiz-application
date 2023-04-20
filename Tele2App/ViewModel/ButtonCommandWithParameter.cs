using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Tele2App.ViewModel
{
    public class ButtonCommandWithParameter : ICommand
    {
        public event EventHandler CanExecuteChanged;

        private Action<object> _action;
        private Func<bool> _canExecute;

        public ButtonCommandWithParameter(Action<object> action, Func<bool> canExecute = null)
        {
            _action = action;
            _canExecute = canExecute;
        }

        public bool CanExecute(object parameter)
        {
            return _canExecute == null || _canExecute();
        }

        public void Execute(object parameter)
        {
            _action(parameter);
        }
    }
}
