# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Test BV module for VMP files."""

from os.path import join as pjoin
import numpy as np
from ..bv_vmp import BvVmpImage, BvVmpHeader
from ...testing import (assert_equal, assert_raises, data_path)
from ...spatialimages import HeaderDataError
from ...externals import OrderedDict

# Example images in format expected for ``test_image_api``, adding ``zooms``
# item.
BVVMP_EXAMPLE_IMAGES = [
    dict(
        fname=pjoin(data_path, 'test.vmp'),
        shape=(1, 10, 10, 10),
        dtype=np.float32,
        affine=np.array([[-3., 0, 0, -21.],
                         [0, 0, -3., -21.],
                         [0, -3., 0, -21.],
                         [0, 0, 0, 1.]]),
        zooms=(3., 3., 3.),
        fileformat=BvVmpImage,
        # These values are from NeuroElf
        data_summary=dict(
            min=0.0033484352752566338,
            max=7.996956825256348,
            mean=3.9617851),
        is_proxy=True),
    dict(
        fname=pjoin(data_path, 'test2.vmp'),
        shape=(2, 10, 10, 10),
        dtype=np.float32,
        affine=np.array([[-3., 0, 0, -21.],
                         [0, 0, -3., -21.],
                         [0, -3., 0, -21.],
                         [0, 0, 0, 1.]]),
        zooms=(3., 3., 3.),
        fileformat=BvVmpImage,
        # These values are from NeuroElf
        data_summary=dict(
            min=0.0033484352752566338,
            max=7.996956825256348,
            mean=3.9617851),
        is_proxy=True),
    dict(
        fname=pjoin(data_path, 'test3.vmp'),
        shape=(1, 5, 4, 3),
        dtype=np.float32,
        affine=np.array([[-2., 0, 0, 122.],
                         [0, 0, -2., 46.],
                         [0, -2., 0, 140.],
                         [0, 0, 0, 1.]]),
        zooms=(2., 2., 2.),
        fileformat=BvVmpImage,
        # These values are from NeuroElf
        data_summary=dict(
            min=0.0,
            max=7.163260459899902,
            mean=2.1438238620758057),
        is_proxy=True)
]

BVVMP_EXAMPLE_HDRS = [
    OrderedDict([('magic_number', 2712847316),
                 ('version', 6),
                 ('document_type', 1),
                 ('nr_of_submaps', 1),
                 ('nr_of_timepoints', 0),
                 ('nr_of_component_params', 0),
                 ('show_params_range_from', 0),
                 ('show_params_range_to', 0),
                 ('use_for_fingerprint_params_range_from', 0),
                 ('use_for_fingerprint_params_range_to', 0),
                 ('x_start', 120),
                 ('x_end', 150),
                 ('y_start', 120),
                 ('y_end', 150),
                 ('z_start', 120),
                 ('z_end', 150),
                 ('resolution', 3),
                 ('dim_x', 256),
                 ('dim_y', 256),
                 ('dim_z', 256),
                 ('vtc_filename', b'test.vtc'),
                 ('prt_filename', b''),
                 ('voi_filename', b''),
                 ('maps',
                  [OrderedDict([('type_of_map', 1),
                                ('map_threshold', 1.649999976158142),
                                ('upper_threshold', 8.0),
                                ('map_name', b'Testmap'),
                                ('pos_min_r', 255),
                                ('pos_min_g', 0),
                                ('pos_min_b', 0),
                                ('pos_max_r', 255),
                                ('pos_max_g', 255),
                                ('pos_max_b', 0),
                                ('neg_min_r', 255),
                                ('neg_min_g', 0),
                                ('neg_min_b', 255),
                                ('neg_max_r', 0),
                                ('neg_max_g', 0),
                                ('neg_max_b', 255),
                                ('use_vmp_color', 0),
                                ('lut_filename', b'<default>'),
                                ('transparent_color_factor', 1.0),
                                ('nr_of_lags', 0),
                                ('display_min_lag', 0),
                                ('display_max_lag', 0),
                                ('show_correlation_or_lag', 0),
                                ('cluster_size_threshold', 50),
                                ('enable_cluster_size_threshold', 0),
                                ('show_values_above_upper_threshold', 1),
                                ('df1', 249),
                                ('df2', 1),
                                ('show_pos_neg_values', 3),
                                ('nr_of_used_voxels', 45555),
                                ('size_of_fdr_table', 0),
                                ('fdr_table_info', []),
                                ('use_fdr_table_index', 0)])]),
                 ('component_time_points', [OrderedDict([('timepoints', [])])]),
                 ('component_params', [])]),
    OrderedDict([('magic_number', 2712847316),
                 ('version', 6),
                 ('document_type', 1),
                 ('nr_of_submaps', 2),
                 ('nr_of_timepoints', 0),
                 ('nr_of_component_params', 0),
                 ('show_params_range_from', 0),
                 ('show_params_range_to', 0),
                 ('use_for_fingerprint_params_range_from', 0),
                 ('use_for_fingerprint_params_range_to', 0),
                 ('x_start', 120),
                 ('x_end', 150),
                 ('y_start', 120),
                 ('y_end', 150),
                 ('z_start', 120),
                 ('z_end', 150),
                 ('resolution', 3),
                 ('dim_x', 256),
                 ('dim_y', 256),
                 ('dim_z', 256),
                 ('vtc_filename', b'test.vtc'),
                 ('prt_filename', b''),
                 ('voi_filename', b''),
                 ('maps',
                  [OrderedDict([('type_of_map', 1),
                                ('map_threshold', 1.649999976158142),
                                ('upper_threshold', 8.0),
                                ('map_name', b'Testmap'),
                                ('pos_min_r', 255),
                                ('pos_min_g', 0),
                                ('pos_min_b', 0),
                                ('pos_max_r', 255),
                                ('pos_max_g', 255),
                                ('pos_max_b', 0),
                                ('neg_min_r', 255),
                                ('neg_min_g', 0),
                                ('neg_min_b', 255),
                                ('neg_max_r', 0),
                                ('neg_max_g', 0),
                                ('neg_max_b', 255),
                                ('use_vmp_color', 0),
                                ('lut_filename', b'<default>'),
                                ('transparent_color_factor', 1.0),
                                ('nr_of_lags', 0),
                                ('display_min_lag', 0),
                                ('display_max_lag', 0),
                                ('show_correlation_or_lag', 0),
                                ('cluster_size_threshold', 50),
                                ('enable_cluster_size_threshold', 0),
                                ('show_values_above_upper_threshold', 1),
                                ('df1', 249),
                                ('df2', 1),
                                ('show_pos_neg_values', 3),
                                ('nr_of_used_voxels', 45555),
                                ('size_of_fdr_table', 0),
                                ('fdr_table_info', []),
                                ('use_fdr_table_index', 0)]),
                   OrderedDict([('type_of_map', 1),
                                ('map_threshold', 1.649999976158142),
                                ('upper_threshold', 8.0),
                                ('map_name', b'Testmap'),
                                ('pos_min_r', 255),
                                ('pos_min_g', 0),
                                ('pos_min_b', 0),
                                ('pos_max_r', 255),
                                ('pos_max_g', 255),
                                ('pos_max_b', 0),
                                ('neg_min_r', 255),
                                ('neg_min_g', 0),
                                ('neg_min_b', 255),
                                ('neg_max_r', 0),
                                ('neg_max_g', 0),
                                ('neg_max_b', 255),
                                ('use_vmp_color', 0),
                                ('lut_filename', b'<default>'),
                                ('transparent_color_factor', 1.0),
                                ('nr_of_lags', 0),
                                ('display_min_lag', 0),
                                ('display_max_lag', 0),
                                ('show_correlation_or_lag', 0),
                                ('cluster_size_threshold', 50),
                                ('enable_cluster_size_threshold', 0),
                                ('show_values_above_upper_threshold', 1),
                                ('df1', 249),
                                ('df2', 1),
                                ('show_pos_neg_values', 3),
                                ('nr_of_used_voxels', 45555),
                                ('size_of_fdr_table', 0),
                                ('fdr_table_info', []),
                                ('use_fdr_table_index', 0)])]),
                 ('component_time_points',
                  [OrderedDict([('timepoints', [])]),
                   OrderedDict([('timepoints', [])])]),
                 ('component_params', [])]),
    OrderedDict([('magic_number', 2712847316),
                 ('version', 6),
                 ('document_type', 1),
                 ('nr_of_submaps', 1),
                 ('nr_of_timepoints', 0),
                 ('nr_of_component_params', 0),
                 ('show_params_range_from', 0),
                 ('show_params_range_to', 0),
                 ('use_for_fingerprint_params_range_from', 0),
                 ('use_for_fingerprint_params_range_to', 0),
                 ('x_start', 102),
                 ('x_end', 108),
                 ('y_start', 54),
                 ('y_end', 62),
                 ('z_start', 62),
                 ('z_end', 72),
                 ('resolution', 2),
                 ('dim_x', 256),
                 ('dim_y', 256),
                 ('dim_z', 256),
                 ('vtc_filename', b'/path/to/test.vtc'),
                 ('prt_filename', b''),
                 ('voi_filename', b''),
                 ('maps',
                  [OrderedDict([('type_of_map', 3),
                                ('map_threshold', 0.16120874881744385),
                                ('upper_threshold', 0.800000011920929),
                                ('map_name', b'<CROSS-CORRELATION>'),
                                ('pos_min_r', 0),
                                ('pos_min_g', 0),
                                ('pos_min_b', 100),
                                ('pos_max_r', 0),
                                ('pos_max_g', 0),
                                ('pos_max_b', 255),
                                ('neg_min_r', 100),
                                ('neg_min_g', 100),
                                ('neg_min_b', 50),
                                ('neg_max_r', 200),
                                ('neg_max_g', 200),
                                ('neg_max_b', 100),
                                ('use_vmp_color', 0),
                                ('lut_filename', b'<default>'),
                                ('transparent_color_factor', 1.0),
                                ('nr_of_lags', 8),
                                ('display_min_lag', 0),
                                ('display_max_lag', 7),
                                ('show_correlation_or_lag', 0),
                                ('cluster_size_threshold', 4),
                                ('enable_cluster_size_threshold', 0),
                                ('show_values_above_upper_threshold', 1),
                                ('df1', 254),
                                ('df2', 0),
                                ('show_pos_neg_values', 3),
                                ('nr_of_used_voxels', 78498),
                                ('size_of_fdr_table', 8),
                                ('fdr_table_info',
                                 [OrderedDict([('q', 0.10000000149011612),
                                               ('crit_standard',
                                                0.13649293780326843),
                                               ('crit_conservative',
                                                0.20921018719673157)]),
                                  OrderedDict([('q', 0.05000000074505806),
                                               ('crit_standard',
                                                0.16120874881744385),
                                               ('crit_conservative',
                                                0.2241515964269638)]),
                                  OrderedDict([('q', 0.03999999910593033),
                                               ('crit_standard',
                                                0.16819879412651062),
                                               ('crit_conservative',
                                                0.2286316156387329)]),
                                  OrderedDict([('q', 0.029999999329447746),
                                               ('crit_standard',
                                                0.1767669916152954),
                                               ('crit_conservative',
                                                0.2341766357421875)]),
                                  OrderedDict([('q', 0.019999999552965164),
                                               ('crit_standard',
                                                0.1880645751953125),
                                               ('crit_conservative',
                                                0.2415686398744583)]),
                                  OrderedDict([('q', 0.009999999776482582),
                                               ('crit_standard',
                                                0.20535583794116974),
                                               ('crit_conservative',
                                                0.2533867359161377)]),
                                  OrderedDict([('q', 0.004999999888241291),
                                               ('crit_standard',
                                                0.2205917239189148),
                                               ('crit_conservative',
                                                0.2645622491836548)]),
                                  OrderedDict([('q', 0.0010000000474974513),
                                               ('crit_standard',
                                                0.25055694580078125),
                                               ('crit_conservative',
                                                0.2873672842979431)])]),
                                ('use_fdr_table_index', 1)])]),
                 ('component_time_points', [OrderedDict([('timepoints', [])])]),
                 ('component_params', [])])
]


def test_BvVmpHeader_set_data_shape():
    vmp = BvVmpHeader()
    assert_equal(vmp.get_data_shape(), (1, 46, 40, 58))
    vmp.set_data_shape((1, 45, 39, 57))
    assert_equal(vmp.get_data_shape(), (1, 45, 39, 57))

    # Use zyx parameter instead of shape
    vmp.set_data_shape(None, [[57, 240], [52, 178], [59, 191]])
    assert_equal(vmp.get_data_shape(), (1, 61, 42, 44))

    # Change number of submaps
    vmp.set_data_shape(None, None, 5)  # via n parameter
    assert_equal(vmp.get_data_shape(), (5, 61, 42, 44))
    vmp.set_data_shape((3, 61, 42, 44))  # via shape parameter
    assert_equal(vmp.get_data_shape(), (3, 61, 42, 44))

    # raise error when neither shape nor zyx nor n is specified
    assert_raises(HeaderDataError, vmp.set_data_shape, None, None, None)

    # raise error when n is negative
    assert_raises(HeaderDataError, vmp.set_data_shape, (-1, 45, 39, 57))
    assert_raises(HeaderDataError, vmp.set_data_shape, None, None, -1)


def test_BvVmpHeader_set_framing_cube():
    vmp = BvVmpHeader()
    assert_equal(vmp.framing_cube, (256, 256, 256))
    vmp.framing_cube = (512, 512, 512)
    assert_equal(vmp.framing_cube, (512, 512, 512))
    vmp.framing_cube = (512, 513, 514)
    assert_equal(vmp.framing_cube, (512, 513, 514))
