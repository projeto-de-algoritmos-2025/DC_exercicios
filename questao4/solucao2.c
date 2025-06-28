#include <limits.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }

    int len1 = nums1Size;
    int len2 = nums2Size;

    int low = 0, high = len1;
    int partition1, partition2;
    int max_left1, min_right1, max_left2, min_right2;

    while (low <= high) {
        partition1 = (low + high) / 2;
        partition2 = (len1 + len2 + 1) / 2 - partition1;

        max_left1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
        min_right1 = (partition1 == len1) ? INT_MAX : nums1[partition1];

        max_left2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
        min_right2 = (partition2 == len2) ? INT_MAX : nums2[partition2];

        if (max_left1 <= min_right2 && max_left2 <= min_right1) {
            if ((len1 + len2) % 2 == 0) {
                return (fmax(max_left1, max_left2) + fmin(min_right1, min_right2)) / 2.0;
            } else {
                return fmax(max_left1, max_left2);
            }
        } else if (max_left1 > min_right2) {
            high = partition1 - 1;
        } else {
            low = partition1 + 1;
        }
    }
    
    return 0.0;
}
