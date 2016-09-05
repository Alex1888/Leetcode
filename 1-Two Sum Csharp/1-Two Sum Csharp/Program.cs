using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _1_Two_Sum_Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var nums = new int[] { -3, 4, 3, 90};
            int target = 0;
            var s = new Solution();
            var result = s.TwoSum(nums, target);
            Console.Write(string.Format("[{0}, {1}]", result[0], result[1]));
        }
    }

    public class Solution
    {
        public int[] TwoSum(int[] nums, int target)
        {
            var result = new int[] { 0, 1 };
            if (nums.Count() == 2)
            {
                return result;
            }

            var dic = new Dictionary<int, int>();
            var n = nums.Count();
            for(int i = 0; i < n; i++)
            {
                if (dic.ContainsKey(nums[i]))
                {
                    if(2*nums[i] == target)
                    {
                        return new int[] { dic[nums[i]], i };
                    }
                    else
                    {
                        continue;
                    }
                }

                dic.Add(nums[i], i);
            }

            for(int i = 0; i < n; i++)
            {
                if(dic.ContainsKey(target - nums[i]) && target != 2*nums[i])
                {
                    result[0] = i;
                    result[1] = dic[target - nums[i]];
                    break;
                }
            }

            return result;
        }
    }
}
